import re

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox.txt'
hand = open(fname)

for lin in hand :
    lin = lin.rstrip()
    regex = re.findall('^New .* [0-9]+', lin)
    if len(regex) > 0 : print(regex)