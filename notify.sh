./pushbullet.py "$@"
if [ $? -eq 0 ]; then
    if [ $(which wall|wc -l) -gt 0 ]; then
        wall "$@"
    fi
    if [ $(which xmessage|wc -l) -gt 0 ]; then
        xmessage -buttons Close -nearmouse "$@"
    fi
else
    #TODO Add Pushbullet error to notification texts below.
    if [ $(which wall|wc -l) -gt 0 ]; then
        wall "$@ (and error for Pushbullet)"
    fi
    if [ $(which xmessage|wc -l) -gt 0 ]; then
        xmessage -buttons Close -nearmouse "$@ (and error for Pushbullet)"
    fi
fi
