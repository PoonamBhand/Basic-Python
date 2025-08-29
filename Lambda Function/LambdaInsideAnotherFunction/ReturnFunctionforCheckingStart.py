# 8) Return function for checking start
def starts_with(ch):
    return lambda s: s.startswith(ch)
check_a = starts_with('a')
print(check_a("apple"))