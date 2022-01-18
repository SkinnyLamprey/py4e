romeo_array = list()
no_duplicates = list()
sorted = list()

fhand = input('Enter file name: ')
if fhand == '' : fhand = open('romeo.txt')

for line in fhand:
    romeo_array = romeo_array + line.split()
 
for word in romeo_array:
    if word in no_duplicates:
        continue
    no_duplicates.append(word)

sorted = no_duplicates

sorted.sort()

print(sorted)

