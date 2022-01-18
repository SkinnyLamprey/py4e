import re
count = 0
run_tot = 0

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox.txt'
hand = open(fname)

for lin in hand :
    lin = lin.rstrip()
    regex = re.findall('^New Revision: ([0-9]+)', lin)
    if len(regex) < 1 : continue
    count += 1
    run_tot += int(regex[0])
grand_tot = run_tot / count
print(int(grand_tot))