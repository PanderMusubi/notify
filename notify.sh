if [ -e ./gotifypush.py ]; then
    ./gotifypush.py "$@"
fi
if [ -e ./pushbullet.py ]; then
    ./pushbullet.py "$@"
fi
if [ $(which wall|wc -l) -gt 0 ]; then
    wall "$@"
fi
if [ $(which xmessage|wc -l) -gt 0 ]; then
    xmessage -buttons Close -nearmouse "$@"
fi
exit 0
