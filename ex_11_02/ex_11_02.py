fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    if len(lin) < 1 or not lin.startswith('From ') : continue
    colon_pos = lin.find(':')
    hour = lin[colon_pos-2:colon_pos]
    di[hour] = di.get(hour, 0) + 1

tmp = list()
for k, v in di.items() :
    tmp.append((k, v))

tmp.sort()

for k, v in tmp :
    print(k, v)
