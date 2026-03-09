import string

chars_low  = string.ascii_lowercase 
chars_up = string.ascii_uppercase

cipher_txt = input("Enter cipher text:  ")

for i in range(26):
    plain_tx = ""

    for c in cipher_txt:
        if c.isalpha():
            if c.isupper(): #if uppercase
                c_index = chars_up.index(c)
                plain_tx += chars_up[c_index - i]

            else: #lowercase
                c_index = chars_low.index(c)
                plain_tx += chars_low[c_index - i]

        else:
            plain_tx += c
            continue
    
    print(f"SHIFT_{i}: {plain_tx}")