"""
Vigenère cipher
"""
import string

# String of all 26 alphabetical letters in uppercase
ALPHABET = string.digits

def alpha_numera_covert(inpp):
    aplha_dict = { 
        'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18,
        'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26
    }
    numera_dict = { 
        1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R',
        19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'
    }
    
    if (isinstance(inpp, int)):
        output = numera_dict.get(inpp)
    else:
        output = aplha_dict.get(inpp)
    return output

    
def encrypt(plaintext: str, key: str) -> str:
    """
    - Counts the length of the key and stores it in key_count
    - Stores each character of the key string in the array key_arr
    - Iterates through each character of the plaintext while having a counter running to iterate through the 
    key simultaneously
    - Grabs the numeric equivalent of the plaintext character and the simultaneous key character using the helper
    function alpha_numera_convert
    - Add the numeric value of the key character and the plaintext's numeric value and generate a new 
    numeric value which then is converted back to an alphabet using the helper function
    - The converted alphabet is then appended to the string cipher for each iteration
    - Return string cipher
    """
   # TODO:  
    cipher = ''
    key_count = 0
    key_arr = []

    for i in key:
        key_count += 1
        key_arr.append(i)
    count = -1

    for txt in plaintext:
        cipher_numera = 0
        count += 1
        cipher_numera = (alpha_numera_covert(txt) + alpha_numera_covert(key_arr[count])) - 1
        if (cipher_numera > 26):
            cipher_numera = cipher_numera - 26
        cipher += alpha_numera_covert(cipher_numera)
        if (count == (key_count - 1)):
            count = -1
    return cipher

  
def decrypt(ciphertext: str, key: str) -> str:
    """
    - Counts the length of the key and stores it in key_count
    - Stores each character of the key string in the array key_arr
    - Iterates through each character of the cyphertext while having a counter running to iterate through the 
    key simultaneously
    - Grabs the numeric equivalent of the ciphertext character and the simultaneous key character using the helper
    function alpha_numera_convert
    - Subtract the numeric value of the key character from the ciphertext's numeric value and generate a new 
    numeric value which then is converted back to an alphabet using the helper function
    - The converted alphabet is then appended to the string plain for each iteration
    - Return string plain
    """
    # TODO:
    plain = ''
    key_count = 0
    key_arr = []

    for i in key:
        key_count += 1
        key_arr.append(i)
    count = -1

    for txt in ciphertext:
        plain_numera = 0
        count += 1
        plain_numera = (alpha_numera_covert(txt) - alpha_numera_covert(key_arr[count])) + 1
        if (plain_numera < 0):
            plain_numera = plain_numera + 26
        plain += alpha_numera_covert(plain_numera)
        if (count == (key_count - 1)):
            count = -1 
    return plain 


if __name__ == "__main__":
    # You can use this to test, or remove and do your own tests below
    plaintext = "ATTACKATDAWN"
    key = "LEMON"
    expected = "LXFOPVEFRNHR"
    ciphertext = encrypt(plaintext, key)
    assert ciphertext == expected
    test_plain = decrypt(ciphertext, key) 
   # print(test_plain)
    assert plaintext == test_plain
