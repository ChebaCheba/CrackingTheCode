#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_TABLE_SIZE 256

int is_unique(char* word){
    int len = strlen(word);
    char* hash_table;
    hash_table = malloc(sizeof(char)*HASH_TABLE_SIZE);
    for(int i=0; i<len; i++){
        char c = word[i];
        if (hash_table[c] == c){
            free(hash_table);
            return 0;
        } else {
            hash_table[c] = c;
        }
    }
    free(hash_table);
    return 1;
}

int main(int argc, char **argv){
    if (argc < 2){
        printf("Usage: ./is_unique <word>\n");
        return -1;
    }

    char* word = argv[1];
    int valid = is_unique(word);

    if(valid){
        printf("%s has unique characters only\n", word);
    } else {
        printf("%s does not have unique characters only\n", word);
    }
    return 0;
}