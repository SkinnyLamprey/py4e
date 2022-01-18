import string

fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'words.txt'
hand = open(fname)

dic = dict()
for line in hand :
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words :
        dic[word] = dic.get(word, 0) + 1
        
largest_num = 0
for k,v in dic.items() :
    print(k,v)
    if v > largest_num : 
        largest_num = v
        most_freq_word = k

print(f'\nMost frequent word is "{most_freq_word}" appearing {largest_num} times.')

test = input("\nInput word to check if it's in current dictionary: \n")
if test in dic :
    print(f'\n{test} is in current dictionary, appearing {dic[test]} times')
else:
    print(f'\n{test} is not in current dictionary')
    input('Press "Enter" to continue.....')

print('\n')

lis = list(dic.keys())
lis.sort()
for key in lis :
    print(key, dic[key])