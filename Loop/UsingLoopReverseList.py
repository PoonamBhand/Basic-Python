# Q7: Write a program to reverse a list using a loop.
numbers = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print(reversed_list)