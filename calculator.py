num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))  
operation = input("Enter an operation (+, -, *, /): ")  

if operation == "+":
    result = num1 + num2
if operation == "-":
    result = num1 - num2
if operation == "*":
    result = num1 * num2
if operation == "/":
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2

if operation in ["+", "-", "*", "/"]:
    print(f"{int(num1)} {operation} {int(num2)} = {int(result)}" if num1.is_integer() and num2.is_integer() and result.is_integer() else f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid operation!")
