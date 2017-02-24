#!/bin/bash

# creates a new tmux session called camstream (name used in stopstream.sh to kill session) and runs raspvid command. Sends raspivid stream to vlc and starts an http stream at port 12345
tmux new-session -s camstream -d "raspivid -o - -t 0 -n -w 600 -h 400 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=0.0.0.0:12345}' :demux=h264"


