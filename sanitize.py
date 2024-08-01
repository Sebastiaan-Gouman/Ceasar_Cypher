def sanitize_input(input):
    remove_spaces = input.replace(' ', '')
    final_string = remove_spaces.lower()
    return final_string