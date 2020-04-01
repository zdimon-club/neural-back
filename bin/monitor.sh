#!/bin/bash
command -v tmux >/dev/null 2>&1 || { echo >&2 "I require tmux but it's not installed.  Aborting. apt i tmux"; exit 1; }

tmux new-session \; \
 split-window -h \; select-pane -t 0 \; \
 send-keys 'cd neural-back; ./bin/run' C-m \; \
 select-pane -t 1 \; \
 send-keys 'cd ../neural-front; ng serve' C-m \; \
 select-pane -t 2 \; \
