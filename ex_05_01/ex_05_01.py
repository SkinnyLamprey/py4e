total = 0
count = 0
number = 0
while number != "done":
    number = input("Enter a number: ")
    if number != "done":
        try:
            total = total + int(number)
            count += 1
        except:
            print("Invalid input")
    elif number == "done":
        average = total / count
        print(total, count, average)
    
