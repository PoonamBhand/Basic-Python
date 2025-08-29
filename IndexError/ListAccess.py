# 2.Function that safely returns an element from a list

def safe_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Invalid index"

numbers = [1, 2, 3, 4]
print(safe_access(numbers, 2))   # valid index
print(safe_access(numbers, 10))  # invalid index
