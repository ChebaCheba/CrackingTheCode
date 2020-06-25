#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define HASH_TABLE_SIZE 256
#define MAX_WORD_LEN 128

int is_pal(char* str){
    char* ht = malloc(sizeof(char)*HASH_TABLE_SIZE);
    int len = strlen(str);
    int count = 0;
    for(int i=0;i<len;i++){
        if(str[i]==' '){
            continue;
        }
        char c = tolower(str[i]);
        if(ht[c]!=c){
            ht[c]=c;
            count++;
        } else {
            ht[c]=c+1;
            count--;
        }
    }
    free(ht);
    if(count<2){
        return 1;
    }
    return 0;
}

int main(){
    char* inp = malloc(sizeof(char)*MAX_WORD_LEN);
    printf("Write the possible palindrome: ");
    fgets(inp, MAX_WORD_LEN, stdin);
    if (strlen(inp)>0 && inp[strlen(inp)-1]=='\n'){
        inp[strlen(inp)-1]='\0';
    } else {
        printf("There was an error with the input");
        return -1;
    }

    int is = is_pal(inp);
    if(is){
        printf("It is a palindrome!\n");
    } else {
        printf("It is not a palindrome :(\n");
    }
    free(inp);
    return 0;
}