#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* rny_string) {
    int len = strlen(rny_string);
    
    char* answer = (char*)malloc(sizeof(char) * (len * 2 + 1));
    
    int j = 0;
    for (int i = 0; i < len; i++) {
        if (rny_string[i] == 'm') {
            answer[j++] = 'r';
            answer[j++] = 'n';
        } else {
            answer[j++] = rny_string[i];
        }
    }
    
    answer[j] = '\0';
    
    return answer;
}