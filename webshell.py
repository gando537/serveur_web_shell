#!/usr/bin/python3

import os, sys, time

def shell(cmd, shel):
    r, w = os.pipe()
    processid = os.fork()
    if processid == 0:
        os.close(r)
        os.dup2(w, 1)
        os.execvp(shel, [shel, '-c', cmd])
    os.wait()
    os.close(w)
    r = os.fdopen(r)
    str = r.read()
    str = str[:-1]
    return str

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
    if method.startswith('GET') and method[-8:] == 'HTTP/1.1':
        header = """HTTP/1.1 200
Content-Type: text/html; charset=utf-8
Connection: close
Content-Length: """

        html_head = """

<!DOCTYPE html>
<head>
    <title>Hello, world!</title>
    <style type="text/css">div {color : #FF0000;} b {color : #000000;}</style>
</head>
<body>"""
        html_foot = """</body>
</html>"""

        action = ''
        if method.startswith('GET / HTTP/1.1'):
            pid = str(os.getpid())
            action = "ajoute_dans_session_" + pid
        else:
            j = 5
            while j < len(method) and method[j] != '?':
                action += method[j]
                j += 1
            pid = action[len("ajoute_dans_session_"):]
        fil = "/tmp/historique_session" + pid + ".txt"
        fd = os.open(fil, os.O_RDWR | os.O_CREAT | os.O_APPEND)
        act_form = "<form action=" + "\"" + action + "\""
        tim = time.ctime()
        form = act_form + " method=\"get\">" + tim + ' $ ' + """
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
            saisi = escaped_utf8_to_utf8(saisi)
        if method.startswith('GET / HTTP/1.1'):
            time_cmd = ''
        else:
            time_cmd = tim + ' $ ' + "<b>" + saisi + "</b>" + "<br>"
        os.write(fd, time_cmd.encode('utf-8'))
        if len(saisi) > 0:
            shel = shell('echo $SHELL', 'sh')
            res = shell(saisi, shel)
            os.write(fd, res.encode('utf-8'))
            os.write(fd, '\n'.encode('utf-8'))
        size_fich = os.path.getsize(fil)
        os.close(fd)
        file = open(fil, "r")
        nb_line = 0
        hist = ''
        for line in file:
            hist += line + "<br>"
            nb_line += 1
        size = 85 + len(form) + size_fich + (nb_line * 4) + 11 + 78
        file.close()
        html = header + str(size) + html_head + "<div>" + hist + "</div>" + form + html_foot
        index_encode = html.encode('utf-8')
        os.write(1, index_encode)
    else :
        data = "request not supported".encode('utf-8')
        os.write(2, data)