# below comments were to remove punctuation but \t and digits were falling through the filter
# import string

fname = input('Enter filename: ')
if fname == '' : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for lin in hand :
    lin = lin.strip()
    if len(lin) < 1 : continue
    lin = lin.lower()
    #lin = lin.translate(lin.maketrans('', '', string.punctuation))
    for c in lin :
        if c not in alphabet : continue
        di[c] = di.get(c, 0) + 1

sum_li = 0
li = list()
for k, v in di.items() :
    li.append((v, k))
    sum_li = sum_li + v

print(sum_li)
li.sort(reverse=True)   

pc = 0.0
for v, k in li :
    pc = v / sum_li * 100.00
    pc = round(pc, 1)
    print(k, v, pc)