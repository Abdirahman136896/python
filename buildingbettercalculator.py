num1 = float(input("Enter the  first number:"))
operator = input("Enter the operation to perform:")
num2 = float(input("Enter the  second number:"))
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1%num2)
else:
    print("invalid operator entered")

