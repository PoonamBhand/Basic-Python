# Handle IndexError in nested list

nested = [[1, 2], [3, 4, 5]]

try:
    print(nested[1][5])  # Invalid column index
except IndexError:
    print("IndexError: Trying to access out of range element in nested list")
