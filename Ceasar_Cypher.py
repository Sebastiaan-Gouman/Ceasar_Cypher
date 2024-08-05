from sanitize import sanitize_input
from cypher import caesar_cipher
from welcome import welcome_message

welcome_message()

while True:
    choice = input("Choose option (1, 2, 3, 4), 'h' for help or 'q' to quit: ")

    if choice == "q":
        print("Goodbye!")
        break

    if choice == "1":
        to_use = input("text om te gebruiken: ")
        print(sanitize_input(to_use))

    elif choice == "2":
        to_use = input("text om te gebruiken: ")
        shift = int(input("shift om te gebruiken: "))

        # Voorbeeld gebruik
        text = sanitize_input(to_use)
        encrypted_text = caesar_cipher(text, shift)
        print("Versleutelde tekst:", encrypted_text)

    elif choice == "3":
        to_use = input("text om te gebruiken: ")
        shift = int(input("shift om te gebruiken: "))

        decrypted_text = caesar_cipher(to_use, -shift)
        print("Ontsleutelde tekst:", decrypted_text)

    elif choice == "4":
        encrypted_text = input("text om te gebruiken: ")

        num = 0

        for x in range(0, 26):
            decrypted_text = caesar_cipher(encrypted_text, -num)
            print("Brute Force:", decrypted_text)
            num += 1

    elif choice == "h":
        welcome_message()

    else:
        print("Invalid input, try again..")