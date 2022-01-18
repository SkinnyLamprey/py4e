user_in = ''

while user_in != 'Q!' :
    import re
    counter = 0
    dic = dict()
    regstr = ''
    fname = input('Enter filename: ')
    if fname == '' : fname = 'mbox.txt'
    user_in = input('Enter a regular expression: ')
    hand = open(fname)

    for line in hand :
        line = line.rstrip()
        regex = re.findall(user_in, line)
        if len(regex) < 1 : continue
        regstr = str(regex[0])
        dic[regstr] = dic.get(regstr, 0) + 1
        #print(regstr)
        counter += 1
    print(f'{fname} had {counter} lines that matched {user_in}')
    #print(dic)
    counter = 0
    for k, v in dic.items() :
        print(v,k)







# CODE BELOW IS FROM PY4E DISCUSSION
# import re
# lst = list()
# count = 0

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = 'mbox.txt'
# fhand = open(fname)

# inp = input("Enter a regular expression: ")
# for line in fhand:
#     line = line.rstrip()
#     # line = line.split()
#     rgex = re.findall(inp, line)
#     print(rgex)
#     print('FLAG1')
#     if len(rgex) < 1 :
#         continue
#     for x in rgex:
#         print(x)
#         print('FLAG2')
#         lst.append(x)
#         # print(lst)
#         count = count + 1

# print(fname, "had", count, "lines that matched", inp)
