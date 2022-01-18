fhand = open('mbox-short-modify.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' or len(words) < 2: 
        continue
    print(words[2])