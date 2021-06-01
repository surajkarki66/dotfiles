#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of qtile


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

run picom --experimental-backend &
run nitrogen --restore & 
run xfce4-clipman &
run cbatticon -u 2 -l 30 -r 20 -n &
run nm-applet
