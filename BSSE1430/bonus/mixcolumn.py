import tables

def mixColumns(state):
    tmp = [None]*16
    for i in range(4):
        tmp[4*i+0] = tables.mul_2[state[4*i+0]]^tables.mul_3[state[4*i+1]]^state[4*i+2]^state[4*i+3]
        tmp[4*i+1] = state[4*i+0]^tables.mul_2[state[4*i+1]]^tables.mul_3[state[4*i+2]]^state[4*i+3]
        tmp[4*i+2] = state[4*i+0]^state[4*i+1]^tables.mul_2[state[4*i+2]]^tables.mul_3[state[4*i+3]]
        tmp[4*i+3] = tables.mul_3[state[4*i+0]]^state[4*i+1]^state[4*i+2]^tables.mul_2[state[4*i+3]]

    return tmp

def main():
    file_cipher = open("input.txt", "r", encoding="utf-8")
    cipher = file_cipher.read()
    file_cipher.close()
    
    cipher_list = [ord(cipher[i]) for i in range(16)]
    output = mixColumns(cipher_list)
    print(output)

if(__name__ == "__main__"):
    main()