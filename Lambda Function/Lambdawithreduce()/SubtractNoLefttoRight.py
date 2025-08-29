# 7) Subtract numbers left to right
from functools import reduce
nums = [100, 20, 10]
print(reduce(lambda a, b: a-b, nums))