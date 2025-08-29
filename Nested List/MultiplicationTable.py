#Write a Python program to create a 3x3 multiplication table using nested lists.
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]

for row in table:
    print(row)
