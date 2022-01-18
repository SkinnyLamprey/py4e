fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

domain = list()
dicto = dict()
for line in hand :
    if len(line) < 1 or not line.startswith('From ') : continue
    line = line.rstrip()
    at_pos = line.find('@')
    sp_pos = line.find(' ', at_pos)
    # print(at_pos, sp_pos)
    domain = line[at_pos+1:sp_pos]
    dicto[domain] = dicto.get(domain, 0) + 1

print(dicto)