def decode(string):
    """takes in the encoded password and returns the original password.
    Written by Xavier Overs"""

    decoded_string = '' # declare global string variable

    for char in string: # iterate through the characters of the string
        char_num_val = ord(char) # convert character to it's number ascii number value
        decoded_char_num_val = char_num_val + 3 # increase character's ascii number value by 3
        new_char = chr(decoded_char_num_val) # convert back to a string character
        decoded_string += new_char # add to new decoded string

    return decoded_string
