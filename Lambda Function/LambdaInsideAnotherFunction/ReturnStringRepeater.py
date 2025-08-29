# 5) Return string repeater
def repeater(n):
    return lambda s: s*n
repeat = repeater(3)
print(repeat("Hi"))