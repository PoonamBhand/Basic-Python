# Q10: Write a program to catch TypeError exception.
try:
    result = "hello" + 10
except TypeError:
    print("Error: Cannot add string and integer.")
