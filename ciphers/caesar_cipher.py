def encript(password, shift):
    encripted = ""
    password = password.upper()
    for char in password:
        if char >= 'A' and char <= 'z':
            if ord(char)+shift < 91:
                encripted += chr((ord(char)+shift))
            else:
                encripted += chr((ord(char)+shift)%91 + 65)
        else:
            encripted += char

    return encripted

def decript(encripted, shift):
    decripted = ""
    encripted = encripted.lower()
    for char in encripted:
        if char >= 'A' and char <= 'z':
            if ord(char)-shift > 96:
                decripted += chr((ord(char)-shift))
            else:
                decripted += chr(123 - (97 - (ord(char)-shift)))
        else:
            decripted += char

    return decripted
        

def main():
    print("1. Encript message")
    print("2. Decript message")
    print("Others to exit")
    
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        encripted = encript(input("Enter message: "), int(input("Shift: ")))
        print("Encripted text is: ", encripted)

    elif(choice == 2):
        decripted = decript(input("Enter encripted text: "), int(input("Shift: ")))
        print("Decripted text is: ", decripted)
    
    else:
        exit()
    
if __name__ == "__main__":
    while(1):
        main()