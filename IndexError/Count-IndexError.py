# 3.Try accessing indexes beyond list size and count errors

data = [5, 10, 15]
error_count = 0

for i in range(6):
    try:
        print(f"Element at index {i}: {data[i]}")
    except IndexError:
        print(f"Index {i} is invalid")
        error_count += 1

print("Total IndexError occurrences:", error_count)
