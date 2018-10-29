x = 1
print("Select operation.")
print("To Add type +.")
print("To Subtract type -.")
print("To Multiply type *.")
print("To Divide type /.")
print("To Exit type exit.")
while x == 1:
    def add(x, y):
       return x + y

    def subtract(x, y):
       return x - y

    def multiply(x, y):
       return x * y

    def divide(x, y):
       return x / y

    choice = input("Enter choice(+,-,*,/,exit):")
    if choice == '+' or choice == '-' or choice == '*' or choice == '/':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    if choice == '+':
       print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '-':
       print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '*':
       print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '/':
       print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == 'exit':
       x = 0
    else:
       print("Invalid input")
