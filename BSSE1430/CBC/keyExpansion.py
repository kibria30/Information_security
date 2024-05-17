import tables

def g_function(word, counter):
    rotated = word[1:] + word[:1]
    substituted = [tables.s[c] for c in rotated]
    substituted[0] ^= tables.rcon[counter]   
    return substituted

def expandKey(key):
    expandedkey = [None]*176
    words = [[0x00]*4 for _ in range(44)]
    bytecounter = 0
    
    for i in range(len(key)):
        expandedkey[i] = key[i]
            
    for i in range(4):
        for j in range(4):
            words[i][j] = expandedkey[bytecounter]
            bytecounter += 1

    for l in range(4, 44, 1):
        if((l%4)==0):
            result = g_function(words[l-1], l//4)
            for i in range(4):
                words[l][i] = words[l-4][i] ^ result[i]
        else:
            for i in range(4):
                words[l][i] = words[l-4][i] ^ words[l-1][i]
                
    loc = 0
    for i in range(44):
        for j in range(4):
            expandedkey[loc] = words[i][j]
            loc += 1

    return expandedkey