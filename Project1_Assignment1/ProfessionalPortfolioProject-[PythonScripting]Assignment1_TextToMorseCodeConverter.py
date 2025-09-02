# Morse code dictionary
#Professional Portfolio Project-[Python Scripting] Assignment1:Text to Morse Code Converter
#A text-based Python program to convert Strings into Morse Code.
#Questions for this assignment
#Reflection Time:
#This is a place to journal your experience of completing this project.
#This will help you figure out how to improve as a developer.
#Write down how you approached the project. What was hard, what was easy.
# How might you improve for the next project? What was your biggest learning from today?
# What would you do differently if you were to tackle this project again?
#Project Title: String to Morse Code Converter
#Problem Statement:
#Write a text-based Python program that takes any input string from the user and converts it into its equivalent
# Morse Code representation.
#Requirements:
#The program should accept user input (a string).
#Each letter, digit, and supported punctuation should be converted into Morse Code.
#Words should be separated by / in Morse Code.
#If a character is not supported in Morse Code, replace it with ?.
#The program should display the converted Morse Code on the console.
#🔹 Example Mappings
#A → .-
#B → -...
#C → -.-.
#H → ....
#E → .
#L → .-..
#O → ---
#1 → .----
#9 → ----.
#So if you type "HELLO", in Morse Code it becomes:
#.... . .-.. .-.. ---

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def string_to_morse(text):
    """Convert a string into Morse Code"""
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # for unknown characters
    return ' '.join(morse_code)

# Main program
if __name__ == "__main__":
    user_input = input("Enter a string to convert into Morse Code: ")
    result = string_to_morse(user_input)
    print("\n🔹 Morse Code Output:")
    print(result)
