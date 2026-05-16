#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* myString, const char* pat) {
    int answer = 0;
    int len = strlen(myString);
    char* buffer = (char*)malloc(sizeof(char)*(len+1));
    for(int i = 0; i<len;i++){
        if(myString[i] == 'A') {
            buffer[i] = 'B';
        }
        else buffer[i]='A';
    }
    buffer[len] = '\0';
    if(strstr(buffer, pat)) answer = 1;
    else answer = 0;
    free(buffer);
    return answer;
}