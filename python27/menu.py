#!/usr/bin/python
"""This is a menu Example"""

# Peter Robinson
# July 2015

import os
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def is_valid_file(parser, arg):
    """Check if arg is a valid file that already exists on the file
       system.
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def get_parser():
    #    parser = ArgumentParser(description=__doc__,
    #                        formatter_class=ArgumentDefaultsHelpFormatter)
    parser = ArgumentParser(description=__doc__)

    parser.add_argument("-1", "--one",
                        action="store_true",
                        dest="one",
                        default=False,
                        help="This is help for 1")

    parser.add_argument("-2", "--two",
                        action="store_true",
                        dest="two",
                        default=False,
                        help="This is help for 2")

    parser.add_argument("-3", "--three",
                        action="store_true",
                        dest="three",
                        default=False,
                        help="This is help for 3")

    parser.add_argument("-u", "--upload",
                        dest="upload",
                        type=lambda x: is_valid_file(parser, x),
                        help="Help!",
                        metavar="file")

    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    return parser

#
# Main
#
if __name__ == "__main__":
    args = get_parser().parse_args()

#
# Actions based on the arguments provided
#
if (args.one):
    print 'This is One\n'
    exit(1)

if (args.two):
    print 'This is Two\n'
    exit(1)

elif (args.three):
    print 'This is Three\n'
    exit(1)

elif (args.upload):
    print 'You have chosen Upload\n'
    exit(1)
