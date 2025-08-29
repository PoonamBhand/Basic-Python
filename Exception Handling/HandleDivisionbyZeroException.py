# Q1: Write a program to handle division by zero exception.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")