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
    plaintext = input("Enter plaintext: ")
    print("Len of plaintext : ", len(plaintext))
    plaintext_num = [ord(c) for c in plaintext]

    cipher_num = encrypt(plaintext_num, roundKeys)
    print(cipher_num)
    cipher_list = [chr(num)  for num in cipher_num]
    cipher = "".join(cipher_list)
    print("cipher is: ",cipher)
    
def AESdecryption():
    # cipher = input("Enter ciphertext: ")
    cipher_num = [ord(c) for c in cipher]
    plaintext_num = decrypt(cipher_num, roundKeys)
    print(plaintext_num)
    # plaintext = [chr(n) for n in plaintext_num]
    # plaintext = "".join()
    # print(plaintext)

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