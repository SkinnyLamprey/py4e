def compute_pay(hours, rate):
    if hours > 40:
        regular_pay = hours * rate
        overtime_pay = (hours - 40) * (rate * 0.5)
        pay = regular_pay + overtime_pay
    else:    
        pay = hours * rate
    return pay


str_hours = input("Enter Hours: ")
str_rate = input("Enter Rate: ")
try:
    float_hours = float(str_hours)
    float_rate = float(str_rate)
except:
    print("Error, please enter numeric input.")
    quit()

gross_pay = compute_pay(float_hours, float_rate)

print("Pay", gross_pay)