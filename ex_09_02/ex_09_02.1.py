fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

dicto = dict() 
for line in hand :
    line = line.split()
    if len(line) < 1 or line[0] == 'From:' : continue
    elif line[0] == 'From' :
        day = line[2]
        dicto[day] = dicto.get(day, 0) + 1

print(dicto)