import tables
import math

def subByteShiftRows(state):
    tmp = [None]*16
    tmp[0] = tables.s[state[0]]
    tmp[4] = tables.s[state[4]]
    tmp[8] = tables.s[state[8]]
    tmp[12] = tables.s[state[12]]
    
    tmp[1] = tables.s[state[5]]
    tmp[5] = tables.s[state[9]]
    tmp[9] = tables.s[state[13]]
    tmp[13] = tables.s[state[1]]
    
    tmp[2] = tables.s[state[10]]
    tmp[6] = tables.s[state[14]]
    tmp[10] = tables.s[state[2]]
    tmp[14] = tables.s[state[6]]
    
    tmp[3] = tables.s[state[15]] 
    tmp[7] = tables.s[state[3]]
    tmp[11] = tables.s[state[7]]
    tmp[15] = tables.s[state[11]]
    
    return tmp
    
def mixColumns(state):
    tmp = [None]*16
    for i in range(4):
        tmp[4*i+0] = tables.mul_2[state[4*i+0]]^tables.mul_3[state[4*i+1]]^state[4*i+2]^state[4*i+3]
        tmp[4*i+1] = state[4*i+0]^tables.mul_2[state[4*i+1]]^tables.mul_3[state[4*i+2]]^state[4*i+3]
        tmp[4*i+2] = state[4*i+0]^state[4*i+1]^tables.mul_2[state[4*i+2]]^tables.mul_3[state[4*i+3]]
        tmp[4*i+3] = tables.mul_3[state[4*i+0]]^state[4*i+1]^state[4*i+2]^tables.mul_2[state[4*i+3]]
    
    return tmp

def addRoundKey(state, roundKey):
    tmp = [None]*16
    for i in range(16):
        tmp[i] = state[i]^roundKey[i] 
    
    return tmp
        

def encrypt(plaintext, roundKeys):
    cnt = 0
    loop = math.ceil((len(plaintext))/16)
    blocksOfText = [[None]*16 for _ in range(loop)]
    
    for i in range(loop):
        if cnt == len(plaintext):
            break
        for j in range(16):
            if cnt == len(plaintext):
                break
            blocksOfText[i][j] = plaintext[cnt]
            cnt += 1

    for i in range(16):
        if(blocksOfText[loop-1][i] == None):
            blocksOfText[loop-1][i] = ord(' ')    #padding with whitespace

    cipher = []
    state = []
    for i in range(len(blocksOfText)):
        state = blocksOfText[i]
        #initial round
        state = addRoundKey(state, roundKeys[0])
        
        # middle rounds 
        for i in range(1, 10, 1):
            state = subByteShiftRows(state)
            state = mixColumns(state)
            state = addRoundKey(state, roundKeys[i])
        
        state = subByteShiftRows(state)
        state = addRoundKey(state, roundKeys[10])
        
        cipher += state
    
    return cipher        