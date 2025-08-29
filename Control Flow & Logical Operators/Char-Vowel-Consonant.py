# Q7: Write a program to check if a character is a vowel or consonant.

ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("The char is Vowel")
else:
    print("The char is Consonant")
