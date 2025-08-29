# Print each element in a nested list

nested = [[10, 20], [30, 40], [50, 60]]

for row in nested:
    for col in row:
        print(col, end=" ")
    print()
