#!/usr/bin/env python3
'''Send push notification over Gotify to multiple tokens.'''

import sys
from os import path, getcwd
from socket import gethostname
from json.decoder import JSONDecodeError

from gotify import gotify, GotifyError

__location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))


def get_tokens():
    '''Get all tokens from file.'''
    tokens = []
    token_file = None
    try:
        token_file = open(path.join(__location__, 'gotify-tokens.txt'))  # pylint:disable=consider-using-with,unspecified-encoding
    except FileNotFoundError:
        try:
            token_file = open('/usr/local/etc/gotify-tokens.txt')  # pylint:disable=consider-using-with,unspecified-encoding
        except FileNotFoundError:
            print('ERROR: Could open tokens file', file=sys.stderr)
            sys.exit(1)
    for line in token_file:
        line = line[:-1]
        if line == '' or line[0] == '#':
            continue
        pair = line.strip().split('\t')
        if pair not in tokens:
            tokens.append(pair)
    if not tokens:
        print('ERROR: Could not find any tokens', file=sys.stderr)
        sys.exit(1)
    return tokens


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERROR: Missing notification text', file=sys.stderr)
        sys.exit(1)

    ERROR = False
    for base_url, token in get_tokens():
        try:
            service = gotify(
                base_url=base_url,
                app_token=token,
            )
            service.create_message(
                ' '.join(sys.argv[1:]),
                title=gethostname(),
                priority=8,
            )
        except (GotifyError, JSONDecodeError): #TODO
            print(f'ERROR: Exception for token {token} with base URL {base_url}', file=sys.stderr)
            ERROR = True

    if ERROR:
        sys.exit(1)
