# 10) Remove empty strings
words = ["hi", "", "python", "", "lambda"]
print(list(filter(lambda w: w != "", words)))