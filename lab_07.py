alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
alpha_len = len(alphabet)

def pretty_print(vsq:list):
    for i, row in enumerate(vsq):
        print(f"| {' | ' .join(row)} |")
        if i == 0:
            suffix = '---|' * (alpha_len + 1)
            print(f'|{suffix}')

def print_header():
    header = [' ']
    #print(f'|   | ', end='')
    for a in alphabet:
        #print(f'{a} |', end=' ')
        header.append(a)
    #print()
    #suffix = '---|' * (alpha_len + 1)
    #print(f'|{suffix}')
    return header

def print_row(a:int):
   row = []
   for c in range(alpha_len):
       row.append(alphabet[(c + a) % alpha_len])
       #print(f'{alphabet[(c + a) % alpha_len]} |', end=' ')
   return row
   #print()

def vigenere_sq():
    sq = []
    header = print_header()
    sq.append(header)
    for a in range(alpha_len):
        #print(f'| {alphabet[a]} | ', end='')
        row = print_row(a)
        row.insert(0, alphabet[a])
        sq.append(row)
        #print(row)
    return sq

def letter_to_index(letter:str, alphabet:str)-> int:
    for i, c in enumerate(alphabet):
        if letter == c:
            return i
    return None

def index_to_letter(index:int, alphabet:str) -> str:
    if 0 <= index < alpha_len:
        return alphabet[index]
    return None

def vigenere_index(key_letter:str, plaintext_letter:str, alphabet:str):
    ci = (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % alpha_len
    return index_to_letter(ci, alphabet)
    #index_to_letter((letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % alpha_len, alphabet)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    pi = (letter_to_index(cipher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % alpha_len
    return index_to_letter(pi, alphabet)
    #C = (K + P) % AL
    #P = (C - K) % AL

def encrypt_vigenere(key:str, plaintext:str, alphabet:str)-> str:
    cipher_text = []
    for i, pt in enumerate(plaintext):
        #print(i, pt, key[i % len(key)])
        cipher_text.append(vigenere_index(key[i%len(key)], pt, alphabet))
    return ''.join(cipher_text)

def decrypt_vigenere(key:str, cipher_text:str, alphabet:str)-> str:
    plaintext = []
    for i, ct in enumerate(cipher_text):
        #print(i, pt, key[i % len(key)])
        plaintext.append(undo_vigenere_index(key[i%len(key)], ct, alphabet))
    return ''.join(plaintext)

#WHZHRCOOEUPNUHOAHLRF

#pretty_print(vigenere_sq())
#print(letter_to_index('Z', alphabet))
#print(index_to_letter(3, alphabet))
#print(vigenere_index('D', 'T', alphabet))
key = 'hi'
#et = encrypt_vigenere(key, plaintext, alphabet)
#pt = decrypt_vigenere(key, et, alphabet)
#print(et,pt)
choice = 0
et_lst = []
while choice != 4:
    choice = int(input("Enter your choice [1,2,3,4]:"))
    if not (1 <= choice <=3):
        continue
    if choice == 1:
        message = input("What is your message?: ")
        et_lst.append(encrypt_vigenere(key, message, alphabet))
        print(et_lst)
    elif choice == 2:
        for ct in et_lst:
            print(decrypt_vigenere(key, ct, alphabet))
    elif choice == 3:
        for ct in et_lst:
            print(f"Here they are:",ct)
    print("Performing...")


