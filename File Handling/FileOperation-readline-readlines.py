# Q8: Using readline and readlines
file = open("sample.txt", "r")
print("First line:", file.readline())
print("All lines as list:", file.readlines())
file.close()
