#! /usr/bin/python3

import argparse
from os import urandom


if __name__ == "__main__":
    RNDLEN = 1000
    PSWLEN = 32
    PSWCOUNT = 10
    BLIST = ['{', '}', '[', ']', '(', ')', '/', '\\', "'", "`",
            '"', '`', '~', ',', ';', ':', '.', '<', '>', ' ', '|']
    parser = argparse.ArgumentParser(
            description="Strong random password generator"
            )
    parser.add_argument(
            '--length',
            '-l',
            type=int,
            default=PSWLEN,
            help="password length"
            )
    parser.add_argument(
            '--count',
            '-c',
            type=int,
            default=PSWCOUNT,
            help="number of generated passwords"
            )
    parser.add_argument(
            '--badchars',
            '-b',
            default=True,
            action="store_false",
            help="ignore bad characters"
            )
    parser.add_argument(
            '--rndlength',
            type=int,
            default=RNDLEN,
            help="random byte count"
            )
    args = parser.parse_args()

    for i in range(args.count):
        rnd = urandom(args.rndlength)
        psw = ""
        for c in rnd:
            if chr(c).isascii() and chr(c).isprintable():
                if args.badchars:
                    if chr(c) not in BLIST:
                        psw += chr(c)
                else:
                    psw += chr(c)
        print(psw[:args.length])
