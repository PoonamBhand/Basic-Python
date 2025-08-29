# Q7: Reading file line by line
file = open("sample.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()
