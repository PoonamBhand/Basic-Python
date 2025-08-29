# Q10: Write a program with a function that takes variable keyword arguments (**kwargs).
def print_details(**details):
    for key, value in details.items():
        print(key, ":", value)

print_details(Name="Ravi", Course="Python", Duration="3 Months")
