import numpy as np
from numpy.linalg import inv

def hill_cipher_2x2_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 == 1:
        plaintext += 'X'

    plaintext_pairs = []
    for i in range(0, len(plaintext), 2):
        pair = [ord(plaintext[i]) - 65, ord(plaintext[i+1]) - 65]
        plaintext_pairs.append(pair)

    key_matrix = np.array(key).reshape(2, 2)
    ciphertext_pairs = []
    
    for pair in plaintext_pairs:
        plaintext_matrix = np.array(pair).reshape(2, 1)
        # Matrix multiplication and modulo 26
        ciphertext_matrix = np.matmul(key_matrix, plaintext_matrix) % 26
        ciphertext_pairs.append(ciphertext_matrix.flatten().tolist())

    ciphertext = ""
    for pair in ciphertext_pairs:
        ciphertext += chr(int(pair[0]) + 65) + chr(int(pair[1]) + 65)
    
    return ciphertext

def hill_cipher_2x2_decrypt(ciphertext, key, size):
    ciphertext_pairs = []
    for i in range(0, len(ciphertext), 2):
        pair = [ord(ciphertext[i]) - 65, ord(ciphertext[i+1]) - 65]
        ciphertext_pairs.append(pair)

    key_matrix = np.array(key).reshape(2, 2)
    # Note: In modular arithmetic, we usually use the modular multiplicative inverse,
    # but for this specific key [[3, 4], [2, 3]], the determinant is 1, so inv() works.
    key_inverse = inv(key_matrix)

    plaintext_pairs = []
    for pair in ciphertext_pairs:
        ciphertext_matrix = np.array(pair).reshape(2, 1)
        # Apply inverse matrix and modulo 26
        plaintext_matrix = np.matmul(key_inverse, ciphertext_matrix) % 26
        plaintext_pairs.append(plaintext_matrix.flatten().tolist())

    plaintext = ""
    for pair in plaintext_pairs:
        # Rounding is necessary because inv() returns floats
        char1 = chr(int(round(pair[0])) + 65)
        char2 = chr(int(round(pair[1])) + 65)
        plaintext += char1 + char2

    return plaintext[:size]

# Execution
plaintext = "HELLO"
size = len(plaintext)
key = [[3, 4], [2, 3]]

ciphertext = hill_cipher_2x2_encrypt(plaintext, key)
decrypted_plaintext = hill_cipher_2x2_decrypt(ciphertext, key, size)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
