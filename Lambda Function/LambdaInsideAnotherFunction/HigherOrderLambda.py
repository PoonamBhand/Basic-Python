# 10) Higher order lambda
def make_math(op):
    if op == "square":
        return lambda x: x**2
    elif op == "double":
        return lambda x: x*2
math_func = make_math("square")
print(math_func(6))