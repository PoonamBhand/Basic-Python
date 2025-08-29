# 4) Minimum number
from functools import reduce
nums = [10, 5, 20]
print(reduce(lambda a, b: a if a < b else b, nums))