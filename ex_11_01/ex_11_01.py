fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand :
    # lin = lin.rstrip()
    if len(lin) < 0 or not lin.startswith('From ') : continue
    words = lin.split()
    email = words[1]
    di[email] = di.get(email, 0) + 1

lis = list()
for k,v in di.items() :
    lis.append((v, k))

lis.sort(reverse=True)
    
for v, k in lis[:len(lis)] :
    print(k, v)

