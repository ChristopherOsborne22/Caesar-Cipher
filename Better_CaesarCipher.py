import string
try:
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value of your choice (any integer will do): "))
    cipher = ''

    if shift < 1:
        print("You have entered a wrong shift value.")

    code = 0
    for char in text:
        if char.isdigit():
            cipher += char
        elif char in string.punctuation:
            code = ord(char)
        elif char.isspace():
            code = ord(" ")
        elif char.islower():
            code = ord(char) + shift
            while code > ord('z'):
                remainder = code - ord('z') - 1
                code = ord('a') + remainder
        elif char.isupper():
            code = ord(char) + shift
            while ord('Z') < code <= ord('a') or ord('a') < code <= ord('z') \
                    or code > ord('z'):
                remainder = code - ord('Z') - 1
                code = ord('A') + remainder
        cipher += chr(code)

    print(cipher)
except ValueError:
    print("You have entered an invalid shift value")
