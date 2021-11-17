def cipher(text, shift, encrypt=True):
    """The cipher function allows you to encrypt text by shifting each letter a certain amount.
    The text input is a string that contains the text to be encrypted. The shift variable is 
    an integer that determines the amount of places each letter should be shifted and replaced with.
    encrypt is a boolean that, when true, leads to encryption of the text. For example,
    if you put in cipher("hello", 3, True), hello will be encrypted as 'khoor'. Then, if you
    were to decrypt the word 'khoor', using -3 for shift, as in cipher("hello", -3, True), would
    decrypt 'khoor' back to 'hello'."""
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text