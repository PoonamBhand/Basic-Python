# Q6: Write a program with multiple return values from a function.
def calculate(a, b):
    return a + b, a - b, a * b

sum_val, diff, prod = calculate(10, 5)
print("Sum:", sum_val)
print("Difference:", diff)
print("Product:", prod)
