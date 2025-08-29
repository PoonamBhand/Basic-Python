# Q11: Write a Python program to flatten a nested list into a single list.
nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for row in nested:
    for val in row:
        flat.append(val)
print("Nested list:", nested)
print("Flattened list:", flat)