# Q10: Write a program to check pass or fail.
# If marks >= 40 → Pass, else Fail and If marks >= 75 → Distinction.

marks = int(input("Enter your marks: "))

if marks >= 40:
    if marks >= 75:
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")
