count = 0
count2 = 0
filename = 'mbox-short.txt' #input('Enter filename: ')
try:
    fhand = open(filename)
except:
    print('Invalid filename!')
    quit()

for line in fhand:
    count += 1
    #print(count)
    line = line.rstrip()
    if line.startswith('From') :
        print(line)
        count2 += 1

print(f'DONE!\n{count2} of {count} lines printed from the below file\n')

# fhand = open(filename)
# inp = fhand.read()
# inp = inp.rstrip()
# print(inp)
# print(f'\nWord count: {len(inp)}\n')