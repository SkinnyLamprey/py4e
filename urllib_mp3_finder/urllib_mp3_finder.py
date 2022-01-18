import re
import urllib.request, urllib.parse, urllib.error

#enter url below
fhand = urllib.request.urlopen('https://www.devinevoices.com/artist/tanga/')

for line in fhand :
    line = line.decode().strip()
    regex = re.findall('.*(http:.*.co.uk           )', line)
    if len(regex) < 1 : continue
    print(regex)
