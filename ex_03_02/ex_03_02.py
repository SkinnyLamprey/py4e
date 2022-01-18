str_hours = input("Enter Hours: ")
str_rate = input("Enter Rate: ")
try:
    float_hours = float(str_hours)
    float_rate = float(str_rate)
except:
    print("Error, please enter numeric input.")
    quit()

float_rate = float(str_rate)
if float_hours > 40:
    #print("Overtime")
    regular_pay = float_hours * float_rate
    overtime_pay = (float_hours - 40) * (float_rate * 0.5)
    pay = regular_pay + overtime_pay
else:    
    pay = float_hours * float_rate
print("xyz Pay", pay)

