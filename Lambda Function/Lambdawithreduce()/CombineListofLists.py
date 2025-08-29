# 8) Combine list of lists
from functools import reduce
lists = [[1,2], [3,4], [5,6]]
print(reduce(lambda a, b: a+b, lists))