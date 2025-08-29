# Q5: Write a program to use else with exception handling.
try:
    num = int("20")
except ValueError:
    print("Error in conversion.")
else:
    print("Conversion successful:", num)

