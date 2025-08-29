# Q4: Write a program to handle multiple exceptions (ZeroDivisionError & ValueError).
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("Result =", num1 / num2)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")