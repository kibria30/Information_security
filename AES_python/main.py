from keyExpansion import expandKey
from AES_encryption import encrypt
from AES_decryption import decrypt

key = "kibriahossenroni"     #input("16 bytes key: ")
key_num = [ord(c) for c in key]
expandedkey = expandKey(key_num)

roundKeys = [[None]*16 for _ in range(11)]
cnt = 0
for i in range(11):
    for j in range(16):
        roundKeys[i][j] = expandedkey[cnt]
        cnt+=1

cipher = ""
def AESencryption():
    file_plain = open("AES_python\plainText.txt", "r")
    plaintext = file_plain.read()
    file_plain.close()
    print("Len of plaintext : ", len(plaintext))
    plaintext_num = [ord(c) for c in plaintext]

    cipher_num = encrypt(plaintext_num, roundKeys)
    print(cipher_num)
    cipher_list = [chr(num)  for num in cipher_num]
    cipher = "".join(cipher_list)
    print("cipher is: ",cipher)
    file_cipher = open("AES_python\cipherText.txt", "w", encoding="utf-8")
    file_cipher.write(cipher)
    file_cipher.close()
    
def AESdecryption():
    file_cipher = open("AES_python\cipherText.txt", "r", encoding="utf-8")
    cipher = file_cipher.read()
    file_cipher.close()
    print(cipher)
    cipher_num = [ord(c) for c in cipher]
    print(cipher_num)
    plaintext_num = decrypt(cipher_num, roundKeys)
    print(plaintext_num)
    plaintext_list = [chr(n) for n in plaintext_num]
    plaintext = "".join(plaintext_list).strip()
    print(plaintext)
    file_decrypted = open("AES_python\decrypted.txt", "w", encoding="utf-8")
    file_decrypted.write(plaintext)
    file_decrypted.close()

def main():
    choice = 1
    while(choice>=0):
        print("1. Encryption\n2. Decryption")
        choice = int(input("Enter your choice(-something for exit): "))
        if(choice<0):
            exit()
        elif(choice==1):
            AESencryption()
        elif(choice==2):
            AESdecryption()

if(__name__ == "__main__"):
    main()