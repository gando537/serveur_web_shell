#!/usr/bin/python3

import os, sys

def escaped_utf8_to_utf8(s):
    res = b'' ; i = 0
    while i < len(s):
        if s[i] == '%':
            res += int(s[i+1:i+3], base=16).to_bytes(1, byteorder='big')
            i += 3
        else :
            res += bytes(s[i], encoding='utf8')
            i += 1
    return res.decode('utf-8')

if __name__ == '__main__':
    data = os.read(0, 100000)
    data_decode = data.decode('utf-8')
    method, headers = data_decode.split('\r\n',1)
    fd = os.open("/tmp/historique.txt", os.O_RDWR | os.O_CREAT | os.O_APPEND)
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

        form = """<form action="ajoute" method="get">
        <input type="text" name="saisie" value="Tapez quelque chose" />
        <input type="submit" name="send" value="&#9166;">
    </form>"""
        saisi = ''
        i = method.find('=')
        if i != -1 :
            while i < len(method) and method[i + 1] != '&':
                if method[i + 1] == '+':
                    saisi += ' '
                else:
                    saisi += method[i + 1]
                i += 1
            saisi = escaped_utf8_to_utf8(saisi) + '<br>'
        if len(saisi) > 4:
            os.write(fd, saisi.encode('utf-8'))
        size_fich = os.path.getsize("/tmp/historique.txt")
        os.close(fd)
        file = open('/tmp/historique.txt', "r")
        hist = ''
        for line in file:
            hist += line
        size = 85 + len(form) + size_fich
        file.close()
        html = header + str(size) + html_head + hist + form + html_foot
        index_encode = html.encode('utf-8')
        os.write(1, index_encode)
    else :
        data = "request not supported".encode('utf-8')
        os.write(2, data)
        sys.exit(0)