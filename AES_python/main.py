from keyExpansion import expandKey
from AES_encryption import encrypt
from AES_decryption import decrypt
from display_manual import display_manual

def keyHandling():
    file_key = open("AES_python\original_key.txt", "r", encoding="utf-8")
    key = file_key.read()
    file_key.close()
    key_num = [ord(c) for c in key]
    expandedkey = expandKey(key_num)

    roundKeys = [[None]*16 for _ in range(11)]
    cnt = 0
    for i in range(11):
        for j in range(16):
            roundKeys[i][j] = expandedkey[cnt]
            cnt+=1
            
    return roundKeys

def AESencryption(roundKeys):
    print("Enter text in \"plainText.txt\" for encryption.")
    file_plain = open("AES_python\plainText.txt", "r")
    plaintext = file_plain.read()
    file_plain.close()
    plaintext_num = [ord(c) for c in plaintext]

    cipher_num = encrypt(plaintext_num, roundKeys)
    cipher_list = [chr(num)  for num in cipher_num]
    cipher = "".join(cipher_list)
    print("cipher is: ",cipher)
    file_cipher = open("AES_python\cipherText.txt", "w", encoding="utf-8")
    file_cipher.write(cipher)
    print("Encryption successful. Cipher stored in \"cipher.txt\"\n")
    file_cipher.close()
    
def AESdecryption(roundKeys):
    print("Enter cipher text in \"cipher.txt\" for decryption")
    file_cipher = open("AES_python\cipherText.txt", "r", encoding="utf-8")
    cipher = file_cipher.read()
    file_cipher.close()
    cipher_num = [ord(c) for c in cipher]
    plaintext_num = decrypt(cipher_num, roundKeys)
    plaintext_list = [chr(n) for n in plaintext_num]
    plaintext = "".join(plaintext_list).strip()
    print("Decrypted text: ",plaintext)
    file_decrypted = open("AES_python\decrypted.txt", "w", encoding="utf-8")
    file_decrypted.write(plaintext)
    print("Decryption successful. Decrypted text stored in \"decrypted.txt\"\n")
    file_decrypted.close()

def main():
    display_manual()
    roundKeys = keyHandling()
    choice = 1
    print("\nLet's start:")
    while(choice>=0):
        print("\t1. Encryption\n\t2. Decryption")
        choice = int(input("\tEnter your choice(-int for exit): "))
        if(choice<0):
            exit()
        elif(choice==1):
            AESencryption(roundKeys)
        elif(choice==2):
            AESdecryption(roundKeys)

if(__name__ == "__main__"):
    main()