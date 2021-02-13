"""
Vigenère cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
Tabula recta: https://en.wikipedia.org/wiki/Tabula_recta
str.index() function: https://docs.python.org/3/library/stdtypes.html#str.index
string library: https://docs.python.org/3/library/string.html

NOTE: We try to make solutions readable NOT efficient
"""
import string

# String of all 26 alphabetical letters in uppercase
ALPHABET = string.ascii_uppercase + " "


def encrypt(plaintext: str, key: str) -> str:
    """
    Vigenère encryption function, see comments below
    """
    ciphertext = ""
    plaintext_len, key_len = len(plaintext), len(key)

    # For each element in the plaintext
    for i in range(plaintext_len):
        # Tabula recta row
        plaintext_index = ALPHABET.index(plaintext[i])
        # Tabula recta column
        # Modulo key_len wraps if plaintext is longer than key
        key_index = ALPHABET.index(key[i % key_len])
        # Append character corresponding to row and column above in Tabula recta
        # Modulo the alphabet length (i.e. row and column length)
        ciphertext += ALPHABET[(plaintext_index + key_index) % 26]

    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    """
    Vigenère decryption function, see comments below
    """
    plaintext = ""
    ciphertext_len, key_len = len(ciphertext), len(key)

    # For each element in the ciphertext
    for i in range(ciphertext_len):
        # Tabula recta row
        ciphertext_index = ALPHABET.index(ciphertext[i])
        # Tabula recta column
        # Modulo key_len wraps if ciphertext is longer than key
        key_index = ALPHABET.index(key[i % key_len])
        # Append character corresponding to row and column above in Tabula recta
        # Modulo the alphabet length (i.e. row and column length)
        # By removing the key_index from the ciphertext_index,
        # we get back the plaintext_index
        plaintext += ALPHABET[(ciphertext_index - key_index) % 26]

    return plaintext


if __name__ == "__main__":
    #  plaintext = "ATTACKATDAWN"
    #  key = "LEMON"
    #  expected = "LXFOPVEFRNHR"
    #  ciphertext = encrypt(plaintext, key)
    #  assert ciphertext == expected
    #  assert plaintext == decrypt(ciphertext, key)
    plaintext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = "LEMON"
    expected = "ELQEHTGWPEZAZTBINGACDSHSEELQZNKCPCT"
    ciphertext = encrypt(plaintext, key)
    assert ciphertext == expected
    assert plaintext == decrypt(ciphertext, key)