# 7) Return map function
def get_incrementor():
    return lambda x: x+1
inc = get_incrementor()
print(list(map(inc, [1,2,3])))