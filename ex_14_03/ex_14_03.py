import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')
if url == '' : url = 'http://py4e-data.dr-chuck.net/comments_1440173.json'

connection = urllib.request.urlopen(url)

data = connection.read().decode()

info = json.loads(data)

running_total = 0
count = 0
for i in range(len(info['comments'])) :
    running_total += info['comments'][i]['count']
    count += 1

print('Count:', count)
print('Sum:', running_total)




