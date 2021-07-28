#!/usr/bin/env python3
'''Send push notification over Pushbullet to multiple accounts.'''

import sys
import os
from socket import gethostname

from asyncio import get_event_loop
from asyncpushbullet import AsyncPushbullet, InvalidKeyError

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                             os.path.dirname(__file__)))

def get_keys():
    '''Get all API keys from the file api-keys.txt.'''
    keys = set()
    with open(os.path.join(__location__, 'api-keys.txt')) as key_file:
        for line in key_file:
            line = line[:-1]
            if line == '' or line[0] == '#':
                continue
            keys.add(line.strip())
    if not keys:
        print('ERROR: Could not find any API key')
        sys.exit(1)
    return keys

async def _notify(key, title, body):
    '''Send notification to Pushbullet.'''
    try:
        async with AsyncPushbullet(key) as apb:
            for device in await apb.async_get_devices():
                if device.icon == 'phone':
                    push = await apb.async_push_note(title=title, body=body,
                                                     device=device)
    except InvalidKeyError as ike:
        print(f'ERROR: Invalid API key {key}')
        return

if len(sys.argv) < 2:
    print('ERROR: Missing notification text')
    sys.exit(1)
loop = get_event_loop()
for key in get_keys():
    loop.run_until_complete(_notify(key, gethostname(),
                                    ' '.join(sys.argv[1:])))

#TODO Return 1 when _notify had an error.
