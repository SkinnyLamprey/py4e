# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

import re
import urllib.request, urllib.parse, urllib.error

#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#fhand = urllib.request.urlopen('http://www.zov.pt/casting/TT649')
fhand = urllib.request.urlopen('https://soundcloud.com/liz-drury-577263964')

for line in fhand :
    line = line.decode().strip()
    regex = re.findall('.*(http:.*.mp3)', line)
    if len(regex) < 1 : continue
    print(regex)
