# Question: Write a program to check whether a number is divisible by 3, 5, both, or none.

# Taking input from the user
num = int(input("Enter a number: "))

# Checking divisibility
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 but not 5")
elif num % 5 == 0:
    print(f"{num} is divisible by 5 but not 3")
else:
    print(f"{num} is not divisible by 3 or 5")
