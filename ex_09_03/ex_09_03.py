fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

dicto = dict()
for line in hand :
    if len(line) < 1 or not line.startswith('From ') : continue
    line = line.split()
    email = line[1]
    dicto[email] = dicto.get(email, 0) + 1
print(dicto)

