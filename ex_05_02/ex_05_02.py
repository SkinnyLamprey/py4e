largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = num
        largest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    else:
        continue
    #print(num)

print('Maximum is', largest)
print('Minimum is', smallest)