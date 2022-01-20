from cgi import print_directory
import urllib.request

char_count = 0
printed_chars = 0

url = input('Enter link: ')
if url == '' : url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line)
    for char in line.decode().strip():
        if char != '\n' :
            print(char, end='')
    # char_count += len(line)
    # if char_count < 3000 :
    #     print(line.decode().strip())
    #     printed_chars += len(line)
    # else :
    #     continue
print(printed_chars)
print(f'There are {char_count} characters in {url}')