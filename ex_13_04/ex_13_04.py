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

url = input('Enter - ')
if url == '' : url = 'http://data.pr4e.org/romeo.txt'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Count all of the paragraph tags
p_count = 0
tags = soup('p')
for tag in tags:
    p_count += 1
    #print(tag.get('href', None))
print(p_count)

# Code: http://www.py4e.com/code3/urllinks.py