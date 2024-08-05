import argparse
from sanitize import sanitize_input
from cypher import caesar_cipher
from welcome import welcome_message

welcome_message()

# Create an argument parser
parser = argparse.ArgumentParser(description='Update dataset.json with a new file.')

# Add the file argument
parser.add_argument('-s', '--sanitize', action='store_true', help='Removes spaces and sets all characters to lower case' )
parser.add_argument('-ec', '--encrypt', action='store_true', help='Encypts text' )
parser.add_argument('-dc', '--decrypt', action='store_true', help='Decrypts text with know shift' )
parser.add_argument('-bf', '--brute_force', action='store_true', help='Brute force decrypted message' )

# Parse the command-line arguments
args = parser.parse_args()

if args.sanitize == True:
    to_use = input("text om te gebruiken: ")
    print(sanitize_input(to_use))

if args.encrypt == True:
    to_use = input("text om te gebruiken: ")
    shift = int(input("shift om te gebruiken: "))

    # Voorbeeld gebruik
    text = sanitize_input(to_use)
    encrypted_text = caesar_cipher(text, shift)
    print("Versleutelde tekst:", encrypted_text)

if args.decrypt == True:
    to_use = input("text om te gebruiken: ")
    shift = int(input("shift om te gebruiken: "))

    decrypted_text = caesar_cipher(to_use, -shift)
    print("Ontsleutelde tekst:", decrypted_text)

if args.brute_force == True:
    encrypted_text = input("text om te gebruiken: ")

    num = 0

    for x in range(0, 26):
        decrypted_text = caesar_cipher(encrypted_text, -num)
        print("Brute Force:", decrypted_text)
        num += 1