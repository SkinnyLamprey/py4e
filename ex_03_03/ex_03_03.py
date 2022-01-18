score = input("Input a score between 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print("Score must be numeric value between 0.0 and 1.0.")
    quit()

if score < 0 or score > 1:
    print(f"Score must be between 0.0 and 1.0.")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print(f"D")
elif score < 0.6:
    print("F")