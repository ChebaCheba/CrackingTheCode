#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int one_way(char* w1, char* w2){
    int len1 = strlen(w1);
    int len2 = strlen(w2);
    
    if (abs(len1-len2)>1) {
        return 0;
    }
    int c1=0;int c2=0;int diff=0;

    while(c1<len1 && c2<len2){
        if(diff > 1){
            return 0;
        }
        if(w1[c1]==w2[c2]){
            c1++;
            c2++;
        } else{
            diff++;
            if(w1[c1+1]==w2[c2+1]){
                c1++;
                c2++;
            } else if(w1[c1+1]==w2[c2]){
                c1++;
            } else if(w1[c1]==w2[c2+1]){
                c2++;
            } else{
                return 0;
            }
        }
    }
    if(diff>1){
        return 0;
    }
    return 1;
}

int main(int argc, char** argv){
    if (argc < 3) {
        printf("Usage: ./one_way <string> <string>\n");
        return -1;
    }

    char* word1 = argv[1];
    char* word2 = argv[2];

    int one = one_way(word1, word2);
    if(one){
        printf("%s and %s are one edit away\n", word1, word2);
    } else{
        printf("%s and %s are not one edit away\n", word1, word2);
    }
}