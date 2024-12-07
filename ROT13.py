import string
def rot13(message):
    alfabeto = string.ascii_letters
    newFrase = ''
    for letter in message:
        letterPos = alfabeto.find(letter)
        if letter in alfabeto:
            if letterPos <26:
                letter = alfabeto[letterPos+13].lower()
                newFrase = newFrase + letter
            else:
                if letterPos > 38:
                    print(letterPos)
                    letterPos = letterPos - 26
                letter = alfabeto[letterPos + 13].upper()
                newFrase = newFrase + letter
        else:
            newFrase = newFrase + letter
    return newFrase

print(rot13("Isso é um teste"))