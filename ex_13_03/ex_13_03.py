from cgi import print_directory
import urllib.request

char_count = 0
printed_chars = 0
flag = True
stop_printing = 3000

url = input('Enter link: ')
if url == '' : url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
for line in fhand:
    display = line.decode().strip()
    char_count += len(line)
    if char_count < stop_printing : 
        print(display)
        printed_chars += len(display)
        len_of_stop = stop_printing - printed_chars
        continue
    elif flag :
        print(display[:len_of_stop])
        printed_chars += len(display[:len_of_stop])
        flag = False
    # print('rem', char_count)
    # print('flag', len(line))
    
print(f'\nNumber of printed characters is {printed_chars}')
print(f'There are {char_count} characters in {url}')