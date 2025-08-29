# Q7: Write a program to handle IndexError exception.
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range.")

