# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if fname == 'na na boo boo':
    print('NA NA BOO BOO is my favourite sound!')
    fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(f'File "{fname}" cannot be opened')
    quit()
count = 0
running = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(':')
    str_num = line[pos+1:]
    num = float(str_num)
    running += num
    #print(line)
    count += 1
print(f"Average spam confidence: {running / count}")