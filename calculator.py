n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
operator = input("Enter operator(+, -, *, /, %, **): ")

if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 - n2)
elif operator == "*":
    print(n1 * n2)
elif operator == "/":
    print("Error: Cannot divide by zero" if n2 == 0 else n1 / n2)
elif operator == "%":
    print("Error: Cannot mod by zero" if n2 == 0 else n1 % n2)
elif operator == "**":
    print(n1 ** n2)
else:
    print("Invalid operator")
