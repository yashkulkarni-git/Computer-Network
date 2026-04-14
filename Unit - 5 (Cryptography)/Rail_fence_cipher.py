def rail_fence_cipher(plaintext, rails):
    plaintext = plaintext.replace(" ", "")
    fence = [[] for i in range(rails)]
    rail = 0
    direction = 1

    for letter in plaintext:
        fence[rail].append(letter)
        rail += direction
        # Change direction at top or bottom rail
        if rail == rails - 1 or rail == 0:
            direction = -direction

    ciphertext = ""
    for rail_content in fence:
        for letter in rail_content:
            ciphertext += letter
            
    return ciphertext

# Example usage
plaintext = "HELLO WORLD"
rails = 3
print("Rail Fence Ciphertext:", rail_fence_cipher(plaintext, rails))
