if [[ "$(tty)" = "/dev/tty1" ]]; then
	startx
fi

eval "$(gh completion -s zsh)"
