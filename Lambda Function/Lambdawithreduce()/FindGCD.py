# 6) Find GCD
from functools import reduce
nums = [48, 64, 16]
print(reduce(lambda a, b: a if b == 0 else reduce(lambda x,y: y if x%y==0 else x%y, [a,b]), nums))

# 7) Subtract numbers left to right
from functools import reduce
nums = [100, 20, 10]
print(reduce(lambda a, b: a-b, nums))