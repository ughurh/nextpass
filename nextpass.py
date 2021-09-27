import secrets  # 3.6+
import sys

CHARS = {
    #'a': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'l': 'abcdefghijklmnopqrstuvwxyz',
    'u': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'n': '0123456789',
    's': '!@#$%^&*()-_+=',  # 14 symbols

    #'x': '0OoLli1',  # similar characters
    'y': '''~`[]{}|\:;"'<>,.?/''',  # additional symbols
    'z': ' '  # space character
}

length_min = 0
length_max = 0
alphabet = ''

# parse arguments
for arg in sys.argv[1:]:
    if arg.isdigit():
        if length_min == 0:
            length_min = int(arg)
        elif length_max == 0:
            # TODO: handle the case lengthmax>lengthmin
            length_max = int(arg)
        else:
            sys.exit('Too many numeric arguments!')
    elif arg.isalpha():
        # TODO: handle duplicate charset types
        for c in arg:
            if c not in CHARS:
                sys.exit('Invalid charset argument!')
            alphabet += CHARS[c] 
    else:
        sys.exit('Invalid Argument!')

# generate password
length = 8
ALPHABET = CHARS['l'] + CHARS['u'] + CHARS['n'] + CHARS['s']

if alphabet == '':
    alphabet = ALPHABET

if length_min > 0:
    length = length_min

if length_max > 0:
    # generte random length
    length = secrets.choice(range(length, length_max))

password = ''.join(secrets.choice(alphabet) for i in range(length))

print('Your next password is:', password)
