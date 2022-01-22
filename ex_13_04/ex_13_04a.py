# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#excercise https://www.py4e.com/tools/python-data/index.php?PHPSESSID=ba847d59ae43f7e22388eb690a489eba

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
span_tag_total = 0
tags = soup('span')
for tag in tags:
    int_convert = int(tag.contents[0])
    span_tag_total += int_convert
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
print(span_tag_total)