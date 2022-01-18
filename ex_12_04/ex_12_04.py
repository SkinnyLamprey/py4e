import re

fname = input('Enter file name: ')
if len(fname) == 0 : fname = 'regex_sum_1440168.txt' 
hand = open(fname)
num_sum = 0

for lin in hand :
    regex = re.findall('[0-9]+', lin)
    if len(regex) > 0 :
        for num in regex: num_sum += int(num)
             
print(num_sum)
