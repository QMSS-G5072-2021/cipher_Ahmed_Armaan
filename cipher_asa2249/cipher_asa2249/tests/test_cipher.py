import pytest as pytest

def cipher(text, shift, encrypt=True):
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


#1a define cipher_test with hello as input and khoor as expected output
def test_cipher():
    actual = cipher("hello", 3, True)
    assert actual == 'khoor', "Should be 'khoor'."

#1b negative shift test function
def test_cipher_negativeidx():
    actual = cipher("hello", -1, True)
    assert actual == "gdkkn", "Should be 'gdkkn'."

#1c text contains nonalphanumeric symbols test
def test_cipher_nonalphanumeric():
    actual = cipher("abc", -1, True)
    assert actual.isalnum(), "Bro you can't put nonalphanumeric characters through this."

#1d add an exception when a 'str' is passed to shift
def cipher(text, shift, encrypt=True):
    assert not isinstance(shift, str), "you can't pass a string to shift"
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

#test that checks for that exception occurring as expected when a string is passed to shift
def test_cipher_stringshift():
    with pytest.raises(AssertionError):
        cipher("abc", "dba", True)
        #exception error is raised, so pytest.raises(AssertionError) runs without an error
