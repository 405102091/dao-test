#!/bin/bash

# prepare ssh server
mkdir -p /var/run/sshd

# start up supervisord, all daemons should launched by supervisord.
/usr/bin/supervisord -c /root/supervisord.conf

tmux new-session -d 'export DISPLAY=":1" && python3 /root/ameblocal.py 2>&1'
# start a shell
/bin/bash
