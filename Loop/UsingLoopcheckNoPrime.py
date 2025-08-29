

# Q9: Write a program to check if a number is prime using a loop.
n = 13
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is prime:", is_prime)

