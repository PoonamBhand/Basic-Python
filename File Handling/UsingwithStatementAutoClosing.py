# Q9: File handling using 'with' (auto-close)
with open("sample.txt", "r") as f:
    print("Inside with block:")
    for line in f:
        print(line.strip())
