import base64
import string
import sympy
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# -------- Caesar --------
def caesar_bruteforce():
    cipher = input("Cipher: ")
    for shift in range(26):
        result = ""
        for c in cipher:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c)-base-shift)%26+base)
            else:
                result += c
        print(f"Shift {shift}: {result}")

# -------- Vigenere --------
def vigenere_decrypt():
    cipher = input("Cipher: ")
    key = input("Key: ").lower()
    result, ki = "", 0
    for c in cipher:
        if c.isalpha():
            shift = ord(key[ki % len(key)]) - 97
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c)-base-shift)%26+base)
            ki += 1
        else:
            result += c
    print(result)

# -------- XOR Single Byte --------
def xor_bruteforce():
    hex_cipher = input("Hex Cipher: ")
    data = bytes.fromhex(hex_cipher)
    for key in range(256):
        decoded = ''.join(chr(b ^ key) for b in data)
        print(f"Key {key}: {decoded}")

# -------- Repeating XOR --------
def xor_repeat():
    cipher_hex = input("Hex Cipher: ")
    key = input("Key: ").encode()
    data = bytes.fromhex(cipher_hex)
    result = ''.join(chr(data[i] ^ key[i % len(key)]) for i in range(len(data)))
    print(result)

# -------- Base64 --------
def base64_decode():
    cipher = input("Base64: ")
    print(base64.b64decode(cipher).decode(errors="ignore"))

# -------- Hash ID --------
def hash_id():
    h = input("Hash: ")
    l = len(h)
    if l == 32:
        print("Likely MD5")
    elif l == 40:
        print("Likely SHA1")
    elif l == 64:
        print("Likely SHA256")
    else:
        print("Unknown")

# -------- RSA Small n --------
def rsa_decrypt():
    n = int(input("n: "))
    e = int(input("e: "))
    c = int(input("c: "))
    factors = sympy.factorint(n)
    p, q = list(factors.keys())
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    print("Decrypted:", m)

# -------- AES ECB --------
def aes_ecb():
    key = input("Key (16 bytes): ").encode()
    cipher = base64.b64decode(input("Base64 Cipher: "))
    cipher_obj = AES.new(key, AES.MODE_ECB)
    print(unpad(cipher_obj.decrypt(cipher), 16).decode())

# -------- Menu --------
while True:
    print("""
1. Caesar Bruteforce
2. Vigenere Decrypt
3. XOR Single-byte Bruteforce
4. Repeating XOR
5. Base64 Decode
6. Hash Identifier
7. RSA Decrypt (small n)
8. AES ECB Decrypt
9. Exit
""")
    choice = input("Choice: ")

    if choice == "1": caesar_bruteforce()
    elif choice == "2": vigenere_decrypt()
    elif choice == "3": xor_bruteforce()
    elif choice == "4": xor_repeat()
    elif choice == "5": base64_decode()
    elif choice == "6": hash_id()
    elif choice == "7": rsa_decrypt()
    elif choice == "8": aes_ecb()
    elif choice == "9": break
    else: print("Invalid")