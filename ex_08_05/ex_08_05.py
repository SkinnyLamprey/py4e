fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0
fh = open(fname)

for line in fh:
    line = line.rstrip()
    line = line.split()
    if len(line) < 1 or line[0] != 'From':
        continue
    print(line[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
