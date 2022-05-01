#!/usr/bin/python3

from operator import truediv
import os, sys
import re
# import pprint
# from io import StringIO

request_string = 'GET / HTTP/1.1\r\nHost: localhost\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: en-US,en;q=0.8'

# # pop the first line so we only process headers
method, headers = request_string.split('\r\n',1)

# print(_)
# # construct a message from the request string
# message = email.message_from_file(StringIO(headers))

# # construct a dictionary containing the headers
# headers = dict(message.items())

# # pretty-print the dictionary of headers
# pprint.pprint(headers, width=160)

# def parser(str):
#     dico = {}
#     for elm in str:
#         tmp = elm.split(': ')
#         dico[tmp[0]] = tmp[1]
#     return dico


# request_string = 'GET / HTTP/1.1\r\nHost: localhost\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: en-US,en;q=0.8'

# pop the first line so we only process headers
# _, headers = request_string.split('\r\n',1)

# construct a message from the request string
# message = email.message_from_file(StringIO(headers))
# construct a dictionary containing the headers
# payload = headers.split('\r\n')
# headers = parser(payload)

# pretty-print the dictionary of headers
# pprint.pprint(headers, width=160)
# if method.startswith('GET') and method[-8:] == 'HTTP/1.1':
#     print(method[-8:])
# else:
#     print('KO')


# def shell(cmd, shel):
#     r, w = os.pipe()
#     processid = os.fork()
#     if processid == 0:
#         os.close(r)
#         os.dup2(w, 1)
#         os.execvp(shel, [shel, '-c', cmd])
#     os.close(w)
#     r = os.fdopen(r)
#     str = r.read()
#     str = str[:-1]
#     return str

# result = shell('echo $SHELL', 'sh')
# print(result)
# print(shell('echo $SHELL', result))

x = False
res = True if x else False
print(res)