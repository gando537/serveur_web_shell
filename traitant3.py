#!/usr/bin/python3

import os, sys

if __name__ == '__main__':
    data = os.read(0, 100000)
    data_decode = data.decode('utf-8')
    method, headers = data_decode.split('\r\n',1)
    if method.startswith('GET') and method[-8:] == 'HTTP/1.1':
        header = """HTTP/1.1 200
Content-Type: text/html; charset=utf-8
Connection: close
Content-Length: """

        html_head = """

<!DOCTYPE html>
<head>
    <title>Hello, world!</title>
</head>
<body>"""
        html_foot = """</body>
</html>"""
        data_decode = data_decode.replace('\r\n', '<br>')
        size = len(data_decode) + 85
        html = header + str(size) + html_head + data_decode + html_foot
        index_encode = html.encode('utf-8')
        os.write(1, index_encode)
    else :
        data = "request not supported".encode('utf-8')
        os.write(2, data)
        sys.exit(0)