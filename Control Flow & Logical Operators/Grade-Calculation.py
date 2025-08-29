# Q11: Write a program to assign grades based on marks.
# 90-100 → A, 75-89 → B, 50-74 → C, 35-49 → D, below 35 → Fail.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")
