import tables
from AES_encryption import addRoundKey

def decrypt(cipher, roundKeys):
    cnt = 0
    loop =  len(cipher)/16
    print("len: %d, loop: %d", len(cipher), loop)
    # blocksOfText = [[None]*16 for _ in range(loop)]
    
    # for i in range(loop):
    #     if cnt == len(plaintext):
    #         break
    #     for j in range(16):
    #         if cnt == len(plaintext):
    #             break
    #         blocksOfText[i][j] = plaintext[cnt]
    #         cnt += 1
