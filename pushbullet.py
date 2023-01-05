#!/usr/bin/env python3
'''Send push notification over Pushbullet to multiple tokens.'''

import sys
from os import path, getcwd
from socket import gethostname
from time import sleep

from asyncio import get_event_loop
from asyncpushbullet import AsyncPushbullet, InvalidKeyError, HttpError

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def get_tokens():
    '''Get all tokens from file.'''
    tokens = set()
    token_file = None
    try:
        token_file = open(path.join(__location__, 'pushbullet-tokens.txt'))  # pylint:disable=consider-using-with,unspecified-encoding
    except FileNotFoundError:
        try:
            token_file = open('/usr/local/etc/pushbullet-tokens.txt')  # pylint:disable=consider-using-with,unspecified-encoding
        except FileNotFoundError:
            print('ERROR: Could open tokens file', file=sys.stderr)
            sys.exit(1)
    for line in token_file:
        line = line[:-1]
        if line == '' or line[0] == '#':
            continue
        tokens.add(line.strip())
    if not tokens:
        print('ERROR: Could not find any tokens', file=sys.stderr)
        sys.exit(1)
    return tokens


TOKENS = get_tokens()
TOTAL = len(TOKENS)
DONE = 0
ERROR = False


async def _notify(token, title, body):
    '''Send notification to Pushbullet.'''
    try:
        async with AsyncPushbullet(token) as apb:
            for device in await apb.async_get_devices():
                if device.icon == 'phone':
                    _ = await apb.async_push_note(title=title,
                                                  body=body,
                                                  device=device)
    except InvalidKeyError:
        print(f'ERROR: Invalid token {token}', file=sys.stderr)
        global ERROR  # pylint:disable=global-statement
        ERROR = True
    except HttpError:
        print(f'WARNING: Overused token {token}', file=sys.stderr)
    global DONE  # pylint:disable=global-statement
    DONE += 1

if len(sys.argv) < 2:
    print('ERROR: Missing notification text', file=sys.stderr)
    sys.exit(1)
loop = get_event_loop()
for value in TOKENS:
    loop.run_until_complete(_notify(value, gethostname(),
                                    ' '.join(sys.argv[1:])))
while True:
    sleep(.2)
    if DONE == TOTAL:
        break
if ERROR:
    sys.exit(1)
