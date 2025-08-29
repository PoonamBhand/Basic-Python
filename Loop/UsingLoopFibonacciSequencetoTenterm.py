# Q10: Write a program to display Fibonacci sequence up to 10 terms using a loop.
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b