# 6) Return filter function
def get_even_filter():
    return lambda x: x % 2 == 0
even_filter = get_even_filter()
print(list(filter(even_filter, [1,2,3,4])))