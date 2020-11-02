LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encrypt(message, key):
    encryptedM = ''
    for letts in message:
        if letts in LETTERS:
            num = LETTERS.find(letts)
            num += key
            encryptedM +=  LETTERS[num]

    return encryptedM

def decode(message, key):
    decodedM = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decodedM +=  LETTERS[num]

    return decodedM

def main():
    message = input('What message do you need to encrypt or decrypt? ')
    key = int(input('Enter the key, numbered 1-26: '))
    choice = input('Do you want to encrypt or decode? Type E for encrypt or D for decode: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decode(message, key))

if __name__ == '__main__':
    main()
