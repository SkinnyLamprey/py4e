# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

rep_count = 0
pos_count = 0

url = input('Enter URL: ')
requ_rep_count = input('Enter count: ')
requ_rep_count = int(requ_rep_count)
requ_pos = input('Enter position: ')
requ_pos = int(requ_pos)
print(url)
while rep_count != requ_rep_count :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    if rep_count < requ_rep_count :
        # Retrieve anchor tags
        tags = soup('a')
        for tag in tags:
            if pos_count < requ_pos :
                pos_count += 1
                url = tag.get('href', None)
            else : 
                print(url)
                pos_count = 0
                rep_count += 1
                break
        #print('END')    