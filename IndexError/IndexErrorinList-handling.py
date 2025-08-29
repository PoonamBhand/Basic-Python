# 1.Program to demonstrate IndexError handling

my_list = [10, 20, 30]

try:
    print("Element at index 5:", my_list[5])
except IndexError:
    print("IndexError: You tried to access an index that does not exist.")
