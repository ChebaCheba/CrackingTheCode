#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_URL_SIZE 256

char* urlify(char* inp){
    char* url = malloc(sizeof(char)*MAX_URL_SIZE);
    int len = strlen(inp);
    int j = 0;
    for(int i=0;i<len;i++){
        if(inp[i]!=' '){
            url[j]=inp[i];
            j++;
        } else {
            url[j]='%';
            url[j+1]='2';
            url[j+2]='0';
            j+=3;
        }
    }
    url[j]='\0';
    return url;
}

int main(){
    char* inp = malloc(sizeof(char)*MAX_URL_SIZE);
    printf("Write url to urlify: ");
    fgets(inp, MAX_URL_SIZE, stdin);
    if (strlen(inp)>0 && inp[strlen(inp)-1]=='\n'){
        inp[strlen(inp)-1]='\0';
    } else {
        printf("There was an error with the input");
        return -1;
    }
    char* url = urlify(inp);
    printf("URL: %s\n", url);
    
    return 0;
}