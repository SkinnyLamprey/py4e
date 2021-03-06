import socket

url = input('Enter URL - ')
if url == '' : url = 'http://data.pr4e.org/romeo.txt' 
split_url = url.split('/')
host_name = split_url[2]
print('Host name', host_name)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host_name, 80))
except:
    print('Try a different URL')
    quit()
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

chr_count = 0
stop_at = 0
while True:
    data = mysock.recv(500)
    chr_count += len(data)
    if len(data) < 1:
        break
    if chr_count <= 3000 :
        print(data.decode(),end='')
        # print('**********CHR COUNT**********', chr_count)
        stop_at += len(data)
    else : 
        continue
print(f'\n\nDocument stopped printing at {stop_at} characters.')
print('\nNumber of characters in the document is', chr_count)
mysock.close()