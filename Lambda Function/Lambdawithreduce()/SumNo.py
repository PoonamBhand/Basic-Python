# 1) Sum of numbers
from functools import reduce
nums = [1, 2, 3, 4]
print(reduce(lambda a, b: a+b, nums))