#!/usr/bin/python3

import os, sys

if __name__ == '__main__':
    data = os.read(0, 100000)
    os.write(2, data)
    sys.exit(0)