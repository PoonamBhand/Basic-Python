nested = [[1, 2, 3], [4, 5], [6]]
total = 0

for row in nested:
    for val in row:
        total += val

print("Sum of all elements:", total)
