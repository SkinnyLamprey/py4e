filename = 'mbox-short.txt'
fhand = open(filename)
count = 0
upper_case = []

for line in fhand:
    line = line.rstrip()
    print(line.upper())