def generateKey(text, keyword):
    key = keyword
    for x in range(len(text) - len(keyword)):
        if len(key) < len(text):
            key += keyword[x % len(keyword)]
        else:
            break
    return key

def encrypt(text, key):
    encrypted = ""
    for x in range(len(text)):
        if text[x]>='a' and text[x]<='z':
            encrypted += chr((ord(text[x]) - ord("a") + ord(key[x]) - ord("a")) % 26 + ord('a'))
        else:
            encrypted += text[x]

    return encrypted

def decrypt(text, key):
    decrypted = ""
    for x in range(len(text)):
        if text[x]>='a' and text[x]<='z':
            decrypted += chr((26 + ord(text[x]) - ord("a") - (ord(key[x]) - ord("a"))) % 26 + ord("a"))
        else:
            decrypted += text[x]
    return decrypted

def main():
    print("1. Encrypt message")
    print("2. Decrypt message")
    print("Others to exit")
    
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        text = input("Enter text: ").lower()
        keyword = input("Enter keyword: ").lower()
        key = generateKey(text, keyword)
        encrypted = encrypt(text, key)
        print("Encrypted text is: ", encrypted)

    elif(choice == 2):
        text = input("Enter text: ").lower()
        keyword = input("Enter keyword: ").lower()
        key = generateKey(text, keyword)
        decrypted = decrypt(text, key)
        print("Decrypted text is: ", decrypted)
    
    else:
        exit()
    
if __name__ == "__main__":
    while(1):
        main()