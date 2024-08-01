def sanitize_input(input):
    remove_spaces = input.replace(' ', '')
    final_string = remove_spaces.lower()
    return final_string

# print(sanitize_input("Test met spaties"))



# with_spaces = "You got the kind of loving that can be so smooth"
# with_underscores = with_spaces.replace(' ', '')
# print(with_underscores)
# # 'You_got_the_kind_of_loving_that_can_be_so_smooth'
# lower_case = with_underscores.lower()
# print(lower_case)

to_use = "Test met spaties"

def caesar_cipher(text, shift):
    # Resultaat string
    result = ""

    # Loop door elke teken in de input tekst
    for char in text:
        #print(char)
        # Check of het een letter is
        if char.isalpha():
            # Houd de letter hoofdletter of kleine letter
            ascii_offset = ord('a')
            # Verplaats de letter
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            # Voeg de nieuwe letter toe aan de resultaat string
            result += new_char
            #print(result)
        else:
            # Als het geen letter is, voeg het gewoon toe aan de resultaat string
            result += char

    return result

# Voorbeeld gebruik
text = sanitize_input(to_use)
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Versleutelde tekst:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Ontsleutelde tekst:", decrypted_text)

num = 0

for x in range(0, 26):
    decrypted_text = caesar_cipher(encrypted_text, num)
    print("Brute Force:", decrypted_text)
    num +=1