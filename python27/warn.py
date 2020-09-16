#!/usr/bin/env python

import warnings


def warn():
    ''' Example use of warnings '''

    warnings.warn("Hey! This is a warning!", DeprecationWarning)

    warnings.warn(" Hey! Peter! Tried to access a position that doesn't exist in \
array inside some_function.", RuntimeWarning)

if __name__ == '__main__':
    warn()
