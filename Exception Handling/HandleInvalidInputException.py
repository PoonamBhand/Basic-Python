# Q2: Write a program to handle invalid input (non-integer) exception.
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid input, please enter a number.")