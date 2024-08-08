# def sanitize_input(input):
#     remove_spaces = input.replace(' ', '')
#     final_string = remove_spaces.lower()
#     return final_string
#
# print(sanitize_input("Test met spaties"))
#
#
#
# # with_spaces = "You got the kind of loving that can be so smooth"
# # with_underscores = with_spaces.replace(' ', '')
# # print(with_underscores)
# # # 'You_got_the_kind_of_loving_that_can_be_so_smooth'
# # lower_case = with_underscores.lower()
# # print(lower_case)
#
# to_use = input("text om te gebruiken: ")
#
# def caesar_cipher(text, shift):
#     # Resultaat string
#     result = ""
#
#     # Loop door elke teken in de input tekst
#     for char in text:
#         #print(char)
#         # Check of het een letter is
#         if char.isalpha():
#             # Houd de letter hoofdletter of kleine letter
#             ascii_offset = ord('a')
#             # Verplaats de letter
#             new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
#             # Voeg de nieuwe letter toe aan de resultaat string
#             result += new_char
#             #print(result)
#         else:
#             # Als het geen letter is, voeg het gewoon toe aan de resultaat string
#             result += char
#
#     return result
#
# # Voorbeeld gebruik
# text = sanitize_input(to_use)
# shift = 3
# encrypted_text = caesar_cipher(text, shift)
# print("Versleutelde tekst:", encrypted_text)
#
# decrypted_text = caesar_cipher(encrypted_text, -shift)
# print("Ontsleutelde tekst:", decrypted_text)
#
# num = 0
#
# for x in range(0, 26):
#     decrypted_text = caesar_cipher(encrypted_text, -num)
#     print("Brute Force:", decrypted_text)
#     num +=1
#
# -------------------------------------------------------------------
#
# import argparse
# from sanitize import sanitize_input
from cypher import caesar_cipher
# from welcome import welcome_message
#
# welcome_message()
#
# # https://stackoverflow.com/questions/18791882/how-to-make-program-go-back-to-the-top-of-the-code-instead-of-closing
# choice = int(input("choose number"))
#
# if choice == 1:
#     to_use = input("text om te gebruiken: ")
#     print(sanitize_input(to_use))
#
# # Create an argument parser
# parser = argparse.ArgumentParser(description='Update dataset.json with a new file.')
#
# # Add the file argument
# parser.add_argument('-s', '--sanitize', action='store_true', help='Removes spaces and sets all characters to lower case' )
# parser.add_argument('-ec', '--encrypt', action='store_true', help='Encypts text' )
# parser.add_argument('-dc', '--decrypt', action='store_true', help='Decrypts text with know shift' )
# parser.add_argument('-bf', '--brute_force', action='store_true', help='Brute force decrypted message' )
#
# # Parse the command-line arguments
# args = parser.parse_args()
#
# if args.sanitize == True:
#     to_use = input("text om te gebruiken: ")
#     print(sanitize_input(to_use))
#
# if args.encrypt == True:
#     to_use = input("text om te gebruiken: ")
#     shift = int(input("shift om te gebruiken: "))
#
#     # Voorbeeld gebruik
#     text = sanitize_input(to_use)
#     encrypted_text = caesar_cipher(text, shift)
#     print("Versleutelde tekst:", encrypted_text)
#
# if args.decrypt == True:
#     to_use = input("text om te gebruiken: ")
#     shift = int(input("shift om te gebruiken: "))
#
#     decrypted_text = caesar_cipher(to_use, -shift)
#     print("Ontsleutelde tekst:", decrypted_text)
#
# if args.brute_force == True:
#     encrypted_text = input("text om te gebruiken: ")
#
#     num = 0
#
#     for x in range(0, 26):
#         decrypted_text = caesar_cipher(encrypted_text, -num)
#         print("Brute Force:", decrypted_text)
#         num += 1

with open("input.txt") as input:
    brute_force_input = input.read()

print(brute_force_input)

encrypted_text = brute_force_input

num = 0

for x in range(0, 26):
    decrypted_text = caesar_cipher(encrypted_text, -num)
    print("Brute Force:", decrypted_text)
    num += 1

test
test2