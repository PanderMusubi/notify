# Notify

Notify via [Gotify](https://gotify.net/),
[Pushbullet](https://www.pushbullet.com/) and other notification systems

## 1 Gotify

Gotify is a FOSS service to send push notifications to web browsers on computers
a FOSS app on mobile devices.

### 1.1 Files

The script `./gotifypush.py` sends a push notification to Gotify. The
receiving Gotify app tokens are stored in the file
`/usr/local/etc/gotify-tokens.txt` or alternatively in the fallback file
`./gotify-tokens.txt`. This file is ignored by git and lines can be
commented out by starting with `#`. The Python script expects the file with
tokens to be in the same directory as it is. An example is:

    # Peter
    #https://123.123.123.123	aITtbC79A2KfWUc
    # John
    https://123.123.123.123	PIYtbC79A8KfWUa

Note that each token is preceded by the base URL and a tab character.

### 1.2 Account

Create a free account at a self-hosted
[Gotify](https://github.com/gotify/server) service and create an app token in
its web GUI. Add the token to the file `gotify-tokens.txt` as described above.

Reporting warnings and errors via alternative notification systems is
recommended.

### 1.3 Server-side installation

Do the following installation:

    #sudo apt-get -y install python3-setuptools python3-pip python3-wheel
    sudo pip3 install -U gotify

### 1.4 Client-side installation

Install one or more of the following client software:
- Android app F-Droid [Gotify](https://f-droid.org/en/packages/com.github.gotify/)
- Android app Google Play [Gotify](https://play.google.com/store/apps/details?id=com.github.gotify)
- Firefox add-on [Gotify](https://addons.mozilla.org/firefox/addon/gotify)
- Chromium extension [Gotify](https://chrome.google.com/webstore/detail/gotify/defcailckfpgaigaiijligpnjipkhhmg) or [Gotify Push](https://chrome.google.com/webstore/detail/gotify-push/cbegkpikakpajcaoblfkeindhhikpfmd)

Recommendation is to install only one mobile app. All notifications are also
found in the web GUI of the service.

### 1.5 Test

A test can be done with:

    ./gotifypush.py '🟢 Dit is een test. これはテストです。'

## 2 Pushbullet

Pushbullet is a freemium service to send push notifications to web browsers on
computers and a proprietary closed source app on mobile devices.

### 2.1 Files

The script `./pushbullet.py` sends a push notification to Pushbullet. The
receiving Pushbullet access tokens are stored in
`/usr/local/etc/pushbullet-tokens.txt` or alternatively in the fallback file
`./pushbullet-tokens.txt`. This files are ignored by git and lines can be
commented out by starting with `#`. The Python script expects the file with
tokens to be in the same directory as it is. An example is:

    # Peter
    #o.SXuTdImi6lfGGPhA2ShXaxEddGkmDXxb
    # John
    o.NXf48BH0dVucAdsa1wQFJoSm8f2I9s27

### 2.2 Account

Create a free account at [Pushbullet](https://pushbullet.com) and get an access
token on https://www.pushbullet.com/#settings/account and add the token to the
file `pushbullet-tokens.txt` as described above.

Pushbullet will disable a token when more than 500 pushes are send per month for
an account. This will result in an error in the Python script. The next month
the token might be enabled again, but might also be not. In that case, new
access token needs to be created and used in the file with the tokens. The old
token should be removed from that file.

Reporting of these kind of errors and other warnings and errors via alternative
notification systems is recommended.

### 2.3 Server-side installation

Do the following installation:

    sudo apt-get -y install python3-setuptools python3-pip python3-wheel
    sudo pip3 install -U asyncpushbullet

In case pip3 cannot build wheels for yarl, frozenlist etc., install:

    sudo apt-get -y install python3-yarl python3-frozenlist python3-aiohttp

and run the pip3 command again.

### 2.4 Client-side installation

Install one or more of the following client software:
- [Android app Google Play](https://play.google.com/store/apps/details?id=com.pushbullet.android)
- [iOS app](https://itunes.apple.com/app/pushbullet/id810352052)
- [Firefox add-on](https://addons.mozilla.org/firefox/addon/pushbullet)
- [Chromium extension](https://chrome.google.com/webstore/detail/pushbullet/chlffgpmiacpedhhbkiomidkjlcfhogd)

Recommendation is to install only one mobile app. All notifications are also
found at https://www.pushbullet.com/#people

### 2.5 Test

A test can be done with:

    ./pushbullet.py '🟢 Dit is een test. これはテストです。'

## 3 wall

`wall` is a GNU/Linux command line tool to write a message to all users. This is
useful when users are working via SSH on a remote machine.

### 3.1 Server-side installation

The following installation is most of the time not needed as this is package is
installed by default:

    sudo apt-get -y install bsdutils

### 3.2 Test

A test can be done with:

    wall '🟢 Dit is een test. これはテストです。'

## 4 xmessage

`xmessage` is a GNU/Linux command line tool to display a message in the window
manager. This is only useful if the server has a window manager running on which
work or maintenance is being done.

### 4.1 Servers-side installation

Only do the following installation when a window manager is already installed:

    sudo apt-get -y install x11-utils

Usually, this package is already installed when using a window manager.

### 4.2 Test

A test can be done with:

    xmessage -buttons Close -nearmouse '🟢 Dit is een test. これはテストです。'

## 5 Combined

To use a combination of all of the above, use `./notify.sh`. This can be tested
with:

    ./notify.sh '🟢 Dit is een test. これはテストです。'
