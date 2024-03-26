import tables
from AES_encryption import addRoundKey

def inv_shifRowsSubBytes(state):
    temp = [None]*16
    
    temp[0] = tables.inv_s[state[0]]
    temp[4] = tables.inv_s[state[4]]
    temp[8] = tables.inv_s[state[8]]
    temp[12] = tables.inv_s[state[12]]
    
    temp[1] = tables.inv_s[state[13]]
    temp[5] = tables.inv_s[state[1]]
    temp[9] = tables.inv_s[state[5]]
    temp[13] = tables.inv_s[state[9]]
    
    
    temp[2] = tables.inv_s[state[10]]
    temp[6] = tables.inv_s[state[14]]
    temp[10] = tables.inv_s[state[2]]
    temp[14] = tables.inv_s[state[6]]
    
    temp[3] = tables.inv_s[state[7]]
    temp[7] = tables.inv_s[state[11]]
    temp[11] = tables.inv_s[state[15]]
    temp[15] = tables.inv_s[state[3]]
    
    return temp

def inv_mixColumns(state):
    tmp = [None]*16
    for i in range(4):
        tmp[4*i+0] = tables.mul_14[state[4*i+0]]^tables.mul_11[state[4*i+1]]^tables.mul_13[state[4*i+2]]^tables.mul_9[state[4*i+3]]
        tmp[4*i+1] = tables.mul_9[state[4*i+0]]^tables.mul_14[state[4*i+1]]^tables.mul_11[state[4*i+2]]^tables.mul_13[state[4*i+3]]
        tmp[4*i+2] = tables.mul_13[state[4*i+0]]^tables.mul_9[state[4*i+1]]^tables.mul_14[state[4*i+2]]^tables.mul_11[state[4*i+3]]
        tmp[4*i+3] = tables.mul_11[state[4*i+0]]^tables.mul_13[state[4*i+1]]^tables.mul_9[state[4*i+2]]^tables.mul_14[state[4*i+3]]
    
    return tmp


def decrypt(cipher, roundKeys):
    cnt = 0
    loop =  len(cipher)//16
    blocksOfText = [[None]*16 for _ in range(loop)]
    for i in range(loop):
        if cnt == len(cipher):
            break
        for j in range(16):
            if cnt == len(cipher):
                break
            blocksOfText[i][j] = cipher[cnt]
            cnt += 1

    decrypted = []
    state = []
    for i in range(len(blocksOfText)):
        state = blocksOfText[i]
        #initial round
        state = addRoundKey(state, roundKeys[10])
        
        # middle rounds 
        for i in range(9, 0, -1):
            state = inv_shifRowsSubBytes(state)
            state = addRoundKey(state, roundKeys[i])
            state = inv_mixColumns(state)
            
        #final round
        state = inv_shifRowsSubBytes(state)
        state = addRoundKey(state, roundKeys[0])
        
        decrypted += state
    
    return decrypted