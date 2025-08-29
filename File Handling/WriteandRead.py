# Q10: Write and read from the same file
with open("new_file.txt", "w+") as f:
    f.write("This is a new file created using w+ mode.\n")
    f.seek(0)
    print("File content:", f.read())
