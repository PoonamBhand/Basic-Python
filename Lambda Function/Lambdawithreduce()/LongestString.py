# 10) Longest string
from functools import reduce
words = ["hi", "python", "lambda"]
print(reduce(lambda a, b: a if len(a) > len(b) else b, words))