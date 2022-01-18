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

largest_value = 0
most_popular = None
for k,v in dicto.items() :
    if v > largest_value :
        largest_value = v
        most_popular = k
    print(k,v)
#print(most_popular,largest_value)
print(f'\n{most_popular} has the most messages, {largest_value} in total.')

# below is not part of soution for excercise 4, 
# but test of sorted function from Tuples p2

print('\n')

dicto.items()
s = sorted(dicto.items())
print(s)

print('\nSwitch key and value')

tmp = list()
for k, v in dicto.items() :
    tmp.append( (v, k ) )

print(tmp)

print('\nSort values in decending order using reverse')

tmp = sorted(tmp, reverse=True)
print(tmp)