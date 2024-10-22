
#Matthew Inkelaar

def encode(string):
    decoded = ''
    for i in range(0, len(string)):
        if string[i] == '1':
            decoded += '4'
        if string[i] == '2':
            decoded += '5'
        if string[i] == '3':
            decoded += '6'
        if string[i] == '4':
            decoded += '7'
        if string[i] == '5':
            decoded += '8'
        if string[i] == '6':
            decoded += '9'
        if string[i] == '7':
            decoded += '0'
        if string[i] == '8':
            decoded += '1'
        if string[i] == '9':
            decoded += '2'
        if string[i] == '0':
            decoded += '3'
    return decoded




valueA = 0
final = None
while valueA != 3:
    print('Menu')
    print('----------')
    print('1. Encode')
    print('2. Decode')
    print('3. Exit')
    valueA = int(input('Please enter an option:'))

    if valueA == 1:
        final = input('Please enter your password to encode:')
        encode(final)
    if valueA == 2:
        print(f'The encoded password is {final}, and the original password is {decode(final)}.')
