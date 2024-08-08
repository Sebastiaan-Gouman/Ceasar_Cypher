def caesar_cipher(text, shift):
    # End result
    result = ""

    # Loops trough every character of the input text
    for char in text:
        # If you want to see the buildup, uncomment the next line
        # print(char)

        # Checks if the input if a letter or not
        if char.isalpha():
            # Since all characters are lower case, there is no difference in offset
            ascii_offset = ord('a')
            # Moves the letter to it's new place
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            # Adds new letter to the result string
            result += new_char
            # If you want to see the buildup, uncomment the next line
            # print(result)
        else:
            # If the input is not a letter, simply gets added to the result string
            result += char

    return result