#include<stdio.h>
#include<stdlib.h>
#include "AES_C.c"

#define SIZE 10000

int main(){

    unsigned char plaintext[] = "kibria hossen";//, how are you. I am fine.";
    unsigned char expandedKey[] = "1234567890123456";
    unsigned char cipher[SIZE];
    unsigned char decrypted[SIZE];
    AESEncryption(plaintext, expandedKey, cipher);
    printf(cipher);
    printf("\n");

    AESDecryption(cipher, expandedKey, decrypted);
    printf(decrypted);

    return 0;
}

// int main(){

//     unsigned char plaintext[100000];
//     scanf("%s", &plaintext);
//     printf(plaintext);

//     return 0;
// }