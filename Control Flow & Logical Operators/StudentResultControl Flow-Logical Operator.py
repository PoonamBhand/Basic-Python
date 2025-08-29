# Topic: Control Flow + Logical Operator
# Question: Check student result - pass if marks >= 40 and attendance >= 75%

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 35 and attendance >= 50:
    print("Student Passed")
else:
    print("Student Failed")
