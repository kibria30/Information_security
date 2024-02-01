def encrypt(password, shift):
    encrypted = ""
    password = password.upper()
    for char in password:
        if char >= 'A' and char <= 'Z':
            if ord(char)+shift < 91:
                encrypted += chr((ord(char)+shift))
            else:
                encrypted += chr((ord(char)+shift)%91 + 65)
        else:
            encrypted += char

    return encrypted

def decrypt(encrypted, shift):
    decrypted = ""
    encrypted = encrypted.lower()
    for char in encrypted:
        if char >= 'a' and char <= 'z':
            if ord(char)-shift > 96:
                decrypted += chr((ord(char)-shift))
            else:
                decrypted += chr(123 - (97 - (ord(char)-shift)))
        else:
            decrypted += char

    return decrypted
        

def main():
    print("1. Encrypt message")
    print("2. Decrypt message")
    print("Others to exit")
    
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        encrypted = encrypt(input("Enter message: "), int(input("Shift: ")))
        print("Encrypted text is: ", encrypted)

    elif(choice == 2):
        decrypted = decrypt(input("Enter encrypted text: "), int(input("Shift: ")))
        print("Decrypted text is: ", decrypted)
    
    else:
        exit()
    
if __name__ == "__main__":
    while(1):
        main()