# 9) Count digits of concatenated number
from functools import reduce
nums = [1, 2, 3]
num = reduce(lambda a, b: a*10+b, nums)
print(num, "has", len(str(num)), "digits")

