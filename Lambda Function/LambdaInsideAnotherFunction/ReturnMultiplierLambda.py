# 3) Return adder lambda
def adder(n):
    return lambda x: x+n
add5 = adder(5)
print(add5(20))

