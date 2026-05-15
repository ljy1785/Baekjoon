#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char** solution(const char* strArr[], size_t strArr_len) {
    char** answer = (char**)malloc(sizeof(char*) * strArr_len);
    
    int count = 0; 
    
    for (size_t i = 0; i < strArr_len; i++) {
        if (strstr(strArr[i], "ad") == NULL) {
            answer[count] = (char*)malloc(sizeof(char) * (strlen(strArr[i]) + 1));
            strcpy(answer[count], strArr[i]);
            count++;
        }
    }
    
    return answer;
}