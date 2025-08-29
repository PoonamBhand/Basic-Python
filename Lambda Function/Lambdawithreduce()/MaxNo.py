

# 3) Maximum number
from functools import reduce
nums = [10, 50, 30]
print(reduce(lambda a, b: a if a > b else b, nums))

