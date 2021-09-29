#!/usr/bin/env python3
'''Send push notification over Pushbullet to multiple accounts.'''

import sys
from os import path, getcwd
from socket import gethostname
from time import sleep

from asyncio import get_event_loop
from asyncpushbullet import AsyncPushbullet, InvalidKeyError

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def get_keys():
    '''Get all API keys from the file api-keys.txt.'''
    keys = set()
    try:
        with open('/usr/local/etc/pushbullet-api-keys.txt') as key_file:
            for line in key_file:
                line = line[:-1]
                if line == '' or line[0] == '#':
                    continue
                keys.add(line.strip())
    except FileNotFoundError:
        try:
            with open(path.join(__location__, 'api-keys.txt')) as key_file:
                for line in key_file:
                    line = line[:-1]
                    if line == '' or line[0] == '#':
                        continue
                    keys.add(line.strip())
        except FileNotFoundError:
            print('ERROR: Could open API key file')
            sys.exit(1)
    if not keys:
        print('ERROR: Could not find any API key')
        sys.exit(1)
    return keys


KEYS = get_keys()
TOTAL = len(KEYS)
DONE = 0
ERROR = False


async def _notify(key, title, body):
    '''Send notification to Pushbullet.'''
    try:
        async with AsyncPushbullet(key) as apb:
            for device in await apb.async_get_devices():
                if device.icon == 'phone':
                    _ = await apb.async_push_note(title=title,
                                                  body=body,
                                                  device=device)
    except InvalidKeyError:
        print(f'ERROR: Invalid API key {key}')
        global ERROR  # pylint:disable=global-statement
        ERROR = True
    global DONE  # pylint:disable=global-statement
    DONE += 1

if len(sys.argv) < 2:
    print('ERROR: Missing notification text')
    sys.exit(1)
loop = get_event_loop()
for value in KEYS:
    loop.run_until_complete(_notify(value, gethostname(),
                                    ' '.join(sys.argv[1:])))
while True:
    sleep(.2)
    if DONE == TOTAL:
        break
if ERROR:
    sys.exit(1)
