def padding(message_bin):
    msgLen = len(message_bin)
    mod = msgLen%128
    if(mod<112):
        message_bin+=b'\x80'
        for i in range(112-mod-1):
            message_bin+=b'\x00'
    else:
        message_bin+=b'\x80'
        for i in range(128-mod-1):
            message_bin+=b'\x00'
     
    message_bin+=(msgLen*8).to_bytes(16)   #binary in big-endian format
    return message_bin

    
def main():
    file_read = open("SHAInput.txt", 'r', encoding='utf-8')
    message = file_read.read()
    file_read.close()
    print(message)
    print(len(message))
    
    padded = padding(bytes(message, 'utf-8'))
    print(padded)
    # get_binary(padded.hex())
    print(padded.hex())
    # print(len(padded.hex()))
    
    res = ''.join(format(ord(i), '08b') for i in message)
    print("The string after binary conversion : " + str(res))

if __name__=='__main__':
    main()
    
    


# print("The original string is : " + str(test_str))

# using join() + ord() + format()
# # Converting String to binary
# res = ''.join(format(ord(i), '08b') for i in test_str)

# # printing result 
# print("The string after binary conversion : " + str(res))
