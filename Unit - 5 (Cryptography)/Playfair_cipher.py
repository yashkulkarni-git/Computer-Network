def playfair_cipher(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    key_table = []

    # Build the key table
    for letter in key:
        if letter not in key_table and letter != "J":
            key_table.append(letter)
    for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if letter not in key_table:
            key_table.append(letter)
    
    key_table = [key_table[i:i+5] for i in range(0, 25, 5)]

    # Prepare plaintext pairs
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if (i + 1) < len(plaintext) else 'X'
        
        if a == b:
            plaintext_pairs.append(a + 'X')
            i += 1
        else:
            plaintext_pairs.append(a + b)
            i += 2

    ciphertext = ""
    for pair in plaintext_pairs:
        letter1, letter2 = pair[0], pair[1]
        
        # Find coordinates
        coords = [(r, c) for r in range(5) for c in range(5) if key_table[r][c] == letter1]
        row1, col1 = coords[0]
        coords = [(r, c) for r in range(5) for c in range(5) if key_table[r][c] == letter2]
        row2, col2 = coords[0]

        if row1 == row2:
            ciphertext += key_table[row1][(col1+1)%5] + key_table[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += key_table[(row1+1)%5][col1] + key_table[(row2+1)%5][col2]
        else:
            ciphertext += key_table[row1][col2] + key_table[row2][col1]

    return ciphertext

# Example usage
plaintext = "HELLO WORLD"
key = "example"
print("Playfair Ciphertext:", playfair_cipher(plaintext, key))
