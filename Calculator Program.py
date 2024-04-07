num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
opr = input("Enter an operator: ")

if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("Wrong input")