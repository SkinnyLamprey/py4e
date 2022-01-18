import re

# Find 'From ' lines  and print
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('From ', line) :
        print(line)

# Find lines beginning with X- and print
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^X-\S+:', line) :
        print(line)

# Find any numbers add to list and print
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

# Find max X-SPAM Confidence
hand  = open('mbox-short.txt')
numlist = list()
for line in hand : 
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    #print(stuff)
    if len(stuff) != 1 : continue
    #print(stuff)
    num = float(stuff[0])
    numlist.append(num)
print('Maximim:', max(numlist))


x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)