# 7) Palindrome strings
words = ["madam", "apple", "racecar", "hello"]
print(list(filter(lambda w: w == w[::-1], words)))

