# Q4: Writing to a file (file mode: 'w')
file = open("sample.txt", "w")  # creates or overwrites
file.write("Hello, this is Python file handling.\n")
file.write("This file is opened in write mode.")
file.close()
