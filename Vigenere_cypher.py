# beware  the night parade of one hundred demons
# code word Oni

def print_from_index(s,i):
    n= len(s)
    print('|', end='')
    for _ in range(n):
        print(s[i % n] +'|', end = ' ')
        i += 1


def vigenere_sq(alphabet):
   for i in range(0,26):
       print_from_index(alphabet,i)
       print ()

def letter_to_index(alphabet,letter):
    """returns the letter's int position in the alphabet"""
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if l == letter:
            return i

def index_to_letter(alphabet,index):
    """returns letter found at position of index"""
    if 0 <= index <len(alphabet):
        return alphabet[index]
    return -1

def vigenere_index(key_letter,plaintext_letter,alphabet):
    k_index = letter_to_index(alphabet,key_letter)
    p_index = letter_to_index(alphabet,plaintext_letter)
    # print(f'{k_index}: {p_index}')
    c_index = (k_index + p_index) % len(alphabet)
    return index_to_letter(alphabet,c_index)

def baguette_encryption(key,plain_text,alphabet):
    ciphertext = ''
    k_len = len(key)
    for i, l in enumerate(plain_text):
        #f'{i}:{l}'
        ciphertext += vigenere_index(key[i%k_len],l, alphabet)
    return ciphertext
def rev_french_baugette_index(key_letter,cypher_letter,alphabet):
    """ci= cypher text
    ki= key index
    pti= plain text index
    gonna need two functions
    (ci-ki) len(alpha) = pti
    """
    k_index = letter_to_index(alphabet,key_letter)
    p_index = letter_to_index(alphabet,cypher_letter)
    # print(f'{k_index}: {p_index}')
    c_index = (k_index - p_index) % len(alphabet)
    return index_to_letter(alphabet,p_index)

def decrypt_french_baugette(key,cipher_text,alphabet):
    cipher_text = ''
    k_len= len(key)
    for i, c in enumerate(cipher_text):
        key_index = alphabet.index(key[i%k_len])
        cipher_text += vigenere_index(key[i % k_len], c, alphabet)
    return plain_text



alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = input('what is your key:')
plain_text = input('what is your plain_text:')
print(baguette_encryption(key,plain_text,alphabet))

"""#vigenere_sq(alphabet)
key = 'ONI'
plaintext= 'beware the night parade of one hundred demons'
#prdodmnfpsmvwtpgmxodirrhbshb mnubaqzsqhrrub  
print(vigenere_index(key[0],plaintext[0],alphabet))
"""

"""
       for j in range(i,26):
            print(f'{alphabet[j]}', end=' ')
         """