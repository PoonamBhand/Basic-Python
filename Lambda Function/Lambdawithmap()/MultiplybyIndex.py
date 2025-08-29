# 9) Multiply by index
nums = [5, 6, 7]
print(list(map(lambda x, i: x*i, nums, range(len(nums)))))