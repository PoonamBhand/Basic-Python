# Q6: Write a program to use finally block in exception handling.
try:
    print("Trying to open file...")
    f = open("test.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution finished.")
