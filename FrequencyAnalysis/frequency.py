# !/usr/bin/env python3
import string
import vigenere

# String of all 26 alphabetical letters in uppercase
ALPHABET = string.ascii_uppercase
# Letter frequencies: https://en.wikipedia.org/wiki/Letter_frequency
ACTUAL_FREQUENCY = {
    'A':0.082,  # A
    'B':0.015,
    'C':0.028,
    'D':0.043,
    'E':0.13,
    'F':0.022,
    'G':0.02,
    'H':0.062,
    'I':0.07,
    'J':0.0015,
    'K':0.0077,
    'L':0.04,
    'M':0.024,
    'N':0.067,
    'O':0.075,
    'P':0.019,
    'Q':0.00095,
    'R':0.06,
    'S':0.063,
    'T':0.091,
    'U':0.028,
    'V':0.0098,
    'W':0.024,
    'X':0.0015,
    'Y':0.02,
    'Z':0.00074,  # Z
}

def alpha_numera_covert(inpp):
    """
    TODO: 
    - Helper Function which returns the index if a letter is provided and a letter if it's index is provided
    """
    aplha_dict = { 
        'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17,
        'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25
    }
    numera_dict = { 
        0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R',
        18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'
    }
    if (isinstance(inpp, int)):
        output = numera_dict.get(inpp)
    else:
        output = aplha_dict.get(inpp)
    return output

def shift_cipher_decrypt(ciphertext, key):
    """
    TODO: 
    - Helper Function which performs shift cipher decryption on the ciphertext with the letter in the provided key
    """
    result = ''
    for i in ciphertext:
        tempVar = 0
        tempVar = (alpha_numera_covert(i) - alpha_numera_covert(key)) % 26
        
        result += alpha_numera_covert(tempVar)
    return result

def freq_analysis(ciphertext: str, key_size: int) -> str:
    """
    TODO: 
    - Makes a dictionary and stores the ciphertext by indexes of each key's letter
    - Passes in all the grouped data of each index one by one into the guess_letter function and appends the output into a single string and returns it
    """
    main_dict = {}
    keyee = ''
    for i in range(0, key_size):
        temp_arr = []
        check = 1
        for letter in ciphertext:
            if (check > key_size):
                check = 1
            if(check == i + 1):
                temp_arr.append(letter)
            check += 1
        main_dict[i + 1] = temp_arr
    for i in range(0, key_size):
        str_test = ''
        str_test = str_test.join(main_dict.get(i+1))
        keyee += guess_letter(str_test) 
    return (keyee)

def guess_letter(ciphertext: str) -> str:
    """
    TODO: 
    - Takes all the letters in the ciphertext and counts how many times each letter occurs and stores the data into a dictionary
    - Stores the letter which occurred the most times in the variable max_letrr
    - Compares the letter which occured the most times with the 9 most common letters in the alphabet which have a higher than average frequency of atleast 0.06
    - The comparison is done by assuming each 9 of them to possibly be the most occurring letter and finding the key for each one and decrypting the cipher text using
    shift cipher deccryption
    - The decrypted plaintext is passed onto the chi square test and whichever plaintext returns the least che square value, its key is assumed to be the best fit for
    that bag of ciphertext in that particular key index
    """
    # TODO: Replace this with your implementation
    count_dict = {}
    max_val = 0
    max_letrr = ''
    etaoin = 'ETAOINSHR'
    best_fit = ''
    best_chi = 100
    for letter in ciphertext:
        if letter in count_dict:
            count_dict[letter] = count_dict[letter] + 1
        else:
            count_dict[letter] = 1
    for key, val in count_dict.items():
        if(val > max_val):
            max_val = val
            max_letrr = key  
    for etaoins in etaoin:
        sample_eKey = (alpha_numera_covert(max_letrr) - alpha_numera_covert(etaoins) ) % 26
        sample_eKey = alpha_numera_covert(sample_eKey)
        sample_e = shift_cipher_decrypt(ciphertext, sample_eKey)
        eChi = chi_squared_test(sample_e)
        if (eChi < best_chi):
            best_chi = eChi
            best_fit = sample_eKey
    return (best_fit)
    

def chi_squared_test(plaintext: str) -> float:
    """
    TODO: 
    - Counts the total number of letters in the plaintext
    - Keeps a counter on how many times each letter is occuring and uses it along with the total count, and the actual frequencies to calculate 
    the chi value from the given equation in the question
    """
    # TODO: Replace this with your implementation
    counter = 0
    for i in plaintext:
        counter += 1
    chi = 0
    for keyss in ACTUAL_FREQUENCY:
        char_counter = 0
        for i in plaintext:
            if(i == keyss):
                char_counter += 1
        chi += (((char_counter/counter) - ACTUAL_FREQUENCY.get(keyss)) ** 2) / ACTUAL_FREQUENCY.get(keyss)
    return chi

if __name__ == "__main__":
    from test import KEYS, TESTS
    for plaintext in TESTS:
        for key in KEYS:
            ciphertext = vigenere.encrypt(plaintext, key)
            assert key == freq_analysis(ciphertext, len(key))
            print(freq_analysis(ciphertext, len(key)))
            
