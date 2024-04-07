weight = int(input("Enter your weight: "))
age = int(input("Enter your age: "))
if weight > 45 and age > 18:  # in AND operator both operands has to be true then it returns to true.
    print("You are Eligible")
else:
    print("You are not Eligible")