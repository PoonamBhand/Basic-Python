# Q9: Write a program to handle KeyError in a dictionary.
student = {"name": "Ravi"}
try:
    print(student["age"])
except KeyError:
    print("Error: Key not found in dictionary.")