# Notify

Notify via Pushbullet and other notification systems

## 1 Pushbullet

Pushbullet is a freemium service to send push notifications to computers and
mobile devices.

### 1.1 Files

The script `./pushbullet.py` sends a push notifications to Pushbullet. The
receiving Pushbullet API keys are stored in
`/usr/local/etc/pushbullet-api-keys.txt` or alternatively `./api-keys.txt`. This
file is ignored by git and lines can be commented out by starting with `#`. The
Python script expects the file with keys to be in the same directory as it is.
An example is:

    # Peter
    #o.SXuTdImi6lfGGPhA2ShXaxEddGkmDXxb
    # John
    o.NXf48BH0dVucAdsa1wQFJoSm8f2I9s27

### 1.2 Account

Create a free account at [Pushbullet](https://pushbullet.com) and get an access
token on https://www.pushbullet.com/#settings/account and add it to the file
`/usr/local/etc/pushbullet-api-keys.txt` or alternatively `./api-keys.txt`.

Pushbullet will disable keys when more than 500 pushes are send per month for an
account. This will result in an error in the Python script. The next month the
keys might be enabled again, but might also be not. In that case, new API key
needs to be created and used in the file with the keys.

Reporting the error via alternative notification systems is recommended.

### 1.3 Server-side installation

Do the following installation:

    sudo apt-get -y install python3-setuptools python3-pip python3-wheel
    sudo pip3 install --upgrade asyncpushbullet

### 1.4 Client-side installation

Install one or more of the following client software:
- [Android app](https://play.google.com/store/apps/details?id=com.pushbullet.android)
- [iOS app](https://itunes.apple.com/app/pushbullet/id810352052)
- [Firefox add-on](https://addons.mozilla.org/firefox/addon/pushbullet)
- [Chromium extension](https://chrome.google.com/webstore/detail/pushbullet/chlffgpmiacpedhhbkiomidkjlcfhogd)

Recommendation is to install only one mobile app. All notifications are also
found at https://www.pushbullet.com/#people

### 1.5 Test

A test can be done with:

    ./pushbullet.py '🟢 Dit is een test. これはテストです。'

## 2 wall

`wall` is a GNU/Linux command line tool to write a message to all users. This is
useful when users are working via SSH on a remote machine.

### 2.1 Server-side installation

The following installation is most of the time not needed as this is package is
installed by default:

    sudo apt-get -y install bsdutils

### 2.2 Test

A test can be done with:

    wall '🟢 Dit is een test. これはテストです。'

## 3 xmessage

`xmessage` is a GNU/Linux command line tool to display a message in the window
manager. This is only useful if the server has a window manager running on which
work or maintenance is being done.

### 3.1 Servers-side installation

Only do the following installation when a window manager is already installed:

    sudo apt-get -y install x11-utils

Usually, this package is already installed when using a window manager.

### 3.2 Test

A test can be done with:

    xmessage -buttons Close -nearmouse '🟢 Dit is een test. これはテストです。'

## 4 Combined

To use a combination of all of the above, use `./notify.sh`. This can be tested
with:

    ./notify.sh '🟢 Dit is een test. これはテストです。'

Note that this will report errors from Pushbullet via wall and xmessage.
