# Q8: Write a program to raise a custom exception if age < 18.
age = 16
try:
    if age < 18:
        raise Exception("Not eligible to vote")
except Exception as e:
    print("Error:", e)

