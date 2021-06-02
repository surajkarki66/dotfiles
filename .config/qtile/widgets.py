import os
import socket
from libqtile import qtile
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen


class MyWidgets:
    def __init__(self):
        self.colors = [
            ["#292d3e", "#292d3e"],
            ["#434758", "#434758"],
            ["#ffffff", "#ffffff"],
            ["#bc13fe", "#bc13fe"],
            ["#8d62a9", "#8d62a9"],
            ["#668bd7", "#668bd7"],
            ["#e1acff", "#e1acff"],
            ["#000000", "#000000"],
            ["#AD343E", "#AD343E"],
            ["#f76e5c", "#f76e5c"],
            ["#8C19FF", "#8C19FF"],
            ["#9966FF", "#9966FF"],
            ["#f1ffff", "#f1ffff"],
            ["#4c566a", "#4c566a"],
            ["#AA80FF", "#AA80FF"]
        ]

        self.kitty = "kitty"
        self.host = "{0}@{1} ".format(os.environ["USER"], socket.gethostname())

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                background=self.colors[0],
                padding=0,
                scale=0.75
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font="JetBrains Mono",
                fontsize=12,
                margin_y=3,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[2],
                inactive=self.colors[1],
                rounded=False,
                highlight_method="block",
                urgent_alert_method='block',
                urgent_border=self.colors[9],
                this_current_screen_border=self.colors[9],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0],
                disable_drag=False
            ),

            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.WindowTabs(
                foreground=self.colors[6],
                background=self.colors[0],
                padding=0,
            ),


            widget.TextBox(
                text='',
                foreground=self.colors[14],
                background=self.colors[0],
                padding=0,
                fontsize=37
            ),

            widget.TextBox(
                text=" ",
                foreground=self.colors[7],
                background=self.colors[14],
                padding=0,
                fontsize=14
            ),
            widget.TextBox(
                text=self.host,
                foreground=self.colors[7],
                background=self.colors[14],
                padding=5,
                fontsize=13
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[11],
                background=self.colors[14],
                padding=0,
                fontsize=37
            ),

            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                background=self.colors[11],
                padding=0,
                fontsize=14
            ),
            widget.KeyboardLayout(foreground=self.colors[7],
                                  background=self.colors[11],),
            widget.TextBox(
                text='',
                background=self.colors[11],
                foreground=self.colors[10],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text="   ",
                background=self.colors[10],
                padding=0,
                fontsize=14,
                mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                     self.kitty + ' -e sudo pacman -Syu')},
            ),
            widget.CheckUpdates(
                update_interval=1000,
                mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                    self.kitty + ' -e sudo pacman -Syu')},
                background=self.colors[10],
                display_format='{updates}',
                # colour_have_updates=self.colors[0],
                distro="Arch_checkupdates",
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[1],
                background=self.colors[10],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                background=self.colors[1],
                padding=0,
                fontsize=18
            ),

            widget.Clock(
                background=self.colors[1],
                format="%A, %B %d - %H:%M "
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[0],
                background=self.colors[1],
                padding=0,
                fontsize=37
            ),

            widget.TextBox(
                text="  ",
                background=self.colors[0],
                padding=0,
            ),
            widget.Volume(
                background=self.colors[0],
                padding=5
            ),
            widget.Battery(background=self.colors[0],
                           padding=5,
                           format='{char}  {percent:2.0%}  {hour:d}:{min:02d}',
                           charge_char='CHR',
                           discharge_char='DIS',
                           empty_char='EMP',
                           full_char='FUL',
                           unknown_char='UNK'
                           ),
            widget.Systray(
                background=self.colors[0],
                padding=5
            ),
        ]
        return widgets_list

    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()
        return widgets_screen

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=20))]
