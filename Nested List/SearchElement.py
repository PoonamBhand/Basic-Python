
# Q9: Write a Python program to search for an element in a nested list.
nested = [[11, 22], [33, 44, 55], [66]]
target = 44
found = False
for row in nested:
    if target in row:
        found = True
        break
if found:
    print(f"{target} found in nested list")
else:
    print(f"{target} not found")