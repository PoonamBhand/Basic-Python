

# Q8: Write a program to find the largest number in a list using a loop.
numbers = [10, 25, 7, 98, 45]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)