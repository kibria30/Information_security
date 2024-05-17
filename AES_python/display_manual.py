def display_manual():
    manual = '''        ---------------------------------------------------------------------
        |                AES Encryption and Decryption Manual               | 
        |-------------------------------------------------------------------|         
        |- You need to provide the necessary input files as described below.|
        |- The input files must be named as follows:                        |
        |* 'original_key.txt' for the encryption/decryption key             |
        |* 'plainText.txt' for the text to be encrypted                     |
        |* 'cipher.txt' for the encrypted text                              |
        |* 'decrypted.txt' for the decrypted text                           |
        |- Ensure the input files are in the same directory as this script. |
        |                                                                   |
        |                                                                   |
        |### Attention!!! You need to enter original 16 bytes key in        |
        |    "original_key.txt" before running main.py                      |
        |                                                                   |
        |                                                                   |
        |                                                                   |
        |main ->                                                            |
        |       Key expansion()->                                           |
        |                        1. gfunction()->                           |
        |                               > SUBBYTE()                         |
        |                               > SHIFT()                           |
        |                                                                   |
        |       AES encryption()->                                          |
        |                        1. addroundkey()                           |
        |                        2. subBytes()                              |
        |                        3. shiftRows()                             |
        |                        4. mixColumns()                            |
        |                                                                   |
        |        AES decryption()->                                         |
        |                        1. addroundkey()                           |
        |                        2. inv_subBytes()                          |
        |                        3. inv_shiftRows()                         |
        |                        4. inv_mixColumns()                        |
        |                                                                   |
        |                                                                   |
        ---------------------------------------------------------------------'''
        
    print(manual)