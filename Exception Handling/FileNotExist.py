# Q3: Write a program to open a file that does not exist and handle the exception.
try:
    f = open("file_not_exist.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")