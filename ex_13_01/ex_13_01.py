import socket

url = input('Enter URL - ')
if url == '' : url = 'http://data.pr4e.org/romeo.txt'
split_url = url.split('/')
host_name = split_url[2]
print(host_name)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host_name, 80))
except:
    print('Try a different URL')
    quit()
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()