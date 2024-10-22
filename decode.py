def decode(string):
    """takes in the encoded password and returns the original password.
    Written by Xavier Overs"""

    decoded_string = '' # declare global string variable

    for i in range(len(string)):
        if string[i] == '0':
            decoded_string += '7'
        if string[i] == '1':
            decoded_string += '8'
        if string[i] == '2':
            decoded_string += '9'
        if string[i] == '3':
            decoded_string += '0'
        if string[i] == '4':
            decoded_string += '1'
        if string[i] == '5':
            decoded_string += '2'
        if string[i] == '6':
            decoded_string += '3'
        if string[i] == '7':
            decoded_string += '4'
        if string[i] == '8':
            decoded_string += '5'
        if string[i] == '9':
            decoded_string += '6'

    return decoded_string
