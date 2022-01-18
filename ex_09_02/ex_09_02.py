# this version runs but more efficient code is later version 
# ex_09_02.1.py
fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

lst = list()
for line in hand :
    line = line.rstrip()
    line = line.split()
    if len(line) < 1 or line[0] != 'From' :
        continue
    day = line[2:3]
    day = str(day)
    lst.append(day)
    
dicto = dict() 
for weekday in lst :
     dicto[weekday] = dicto.get(weekday, 0) + 1

print(dicto)