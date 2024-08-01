def caesar_cipher(text, shift):
    # Resultaat string
    result = ""

    # Loop door elke teken in de input tekst
    for char in text:
        # print(char)
        # Check of het een letter is
        if char.isalpha():
            # Houd de letter hoofdletter of kleine letter
            ascii_offset = ord('a')
            # Verplaats de letter
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            # Voeg de nieuwe letter toe aan de resultaat string
            result += new_char
            # print(result)
        else:
            # Als het geen letter is, voeg het gewoon toe aan de resultaat string
            result += char

    return result