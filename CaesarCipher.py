'''
This code implements a Caesar cipher that shifts each character 
in the input message by 3 positions. Alphabetic characters are shifted within
the alphabet (e.g., 'a' becomes 'd'), while numbers and special characters 
are shifted by 3 in their ASCII values.
It supports both encoding and decoding of messages.
'''
def storing_all_chars(msg, shift):
    result = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += chr((ord(char) + shift) % 256)
    return result
msg= input()
shift = 3
encoded = storing_all_chars(msg, shift)
decoded = storing_all_chars(encoded, -shift)

print("Original Message:", msg)
print("Encoded Message:", encoded)
print("Final Decoded Message:", decoded)
#input1:
'''
jaya123@
Original Message: jaya123@
Encoded Message: mdbd456C
Final Decoded Message: jaya123Z
'''
#input2:
'''
Agetware
Original Message: Agetware
Encoded Message: Djhwzduh
Final Decoded Message: Agetware
'''
