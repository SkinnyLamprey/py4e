# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'cwen']
# for name in names :
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


# print("\n")


# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
# print(purse['candy'])
# purse['candy'] = purse['candy'] + 2
# purse['candy'] += 2
# purse['tissues'] -= 12
# purse['tissues'] = 12
# print('Purse 1', purse)


# purse2 = { 'money' : 12, 'candy' : 3, 'tissues' : 75 }
# print('Purse 2', purse2)


print('\n')

word_dict = dict()
word_list = list()
fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     #print(line)
#     words = line.split()
#     for word in words:
#         word_list.append(word)

# for word in word_list:
#     if word not in word_dict :
#         word_dict[word] = 1
#     else:
#         word_dict[word] += 1
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print('\nCounts', counts)
for key in counts:
    print(key, counts[key])

print('\n\nList', list(counts))
print('\n\nKeys', counts.keys())
print('\n\nValues', counts.values())
print('\n\nItems', counts.items())

for aaa,bbb in counts.items() :
    print(aaa, bbb)
