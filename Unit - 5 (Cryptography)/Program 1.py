string = "Hello World"
result = ""

for char in string:
# XOR the character with 1
    xor_char = chr(ord(char) ^ 1)
    result += xor_char
    print(result)

