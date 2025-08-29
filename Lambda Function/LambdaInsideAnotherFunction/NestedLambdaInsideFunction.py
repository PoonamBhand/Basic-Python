# 9) Nested lambda inside function
def outer():
    return lambda x: (lambda y: x+y)
f = outer()
print(f(10)(5))