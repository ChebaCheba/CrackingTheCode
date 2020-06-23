#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_TABLE_SIZE 256

char* nowhs(char* word){
    int len = strlen(word);
    int new_len = 0;
    char* clean = malloc(sizeof(char)*len);
    for(int i=0;i<len;i++){
        if(word[i]!=' '){
            clean[i]=word[i];
            new_len++;
        }
    }
    clean[new_len]='\0';
    return clean;
}

int check_perm(char* str1, char* str2){
    char* hash_t = malloc(sizeof(char)*HASH_TABLE_SIZE);
    char* word1 = nowhs(str1);
    char* word2 = nowhs(str2);

    if(strlen(word1)!=strlen(word2)){
        return 0;
    }

    int len = strlen(word1);
    int count = 0;

    for(int i=0;i<len;i++){
        char char1 = word1[i];
        char char2 = word2[i];
        if(char1!=hash_t[char1]){
            hash_t[char1] = char1;
            count++;
        } else
        {
            hash_t[char1] = char1+1;
            count--;
        }
        if(char2!=hash_t[char2]){
            hash_t[char2] = char2;
            count++;
        } else
        {
            hash_t[char2] = char2+1;
            count--;
        }
    }

    if(count!=0){
        return  0;
    }
    return 1;
}

int main(int argc, char **argv){
    if (argc < 3){
        printf("Usage: ./check_perm <string> <string>\n");
        return -1;
    }
    char* word1 = argv[1];
    char* word2 = argv[2];

    int is_perm = check_perm(word1, word2);

    if(is_perm){
        printf("%s is a permutation of %s\n", word1, word2);
    } else {
        printf("%s is not a permutation of %s\n", word1, word2);
    }
    return 0;
}