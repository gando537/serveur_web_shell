#!/usr/bin/python3

import os, sys

if __name__ == '__main__':
    data = os.read(0, 100000)
    data_decode = data.decode('utf-8')
    if data_decode.startswith('GET / HTTP/1.1'):
        os.write(2, data)
    else :
        data = "request not supported".encode('utf-8')
        os.write(2, data)
        sys.exit(0)