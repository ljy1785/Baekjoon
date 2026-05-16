#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 실제 프로그래머스 환경에서는 return_len 파라미터가 주어집니다.
int* solution(const char* myString) {
    int len = strlen(myString);

    int x_count = 0;
    for(int i = 0; i < len; i++){
        if(myString[i] == 'x') x_count++;
    }
    
    // 1. calloc 문법 수정 (인자를 두 개로 분리)
    int* answer = (int*)calloc(x_count + 1, sizeof(int));
    
    // 2. 채점 시스템에 반환할 배열의 길이 알려주기
    // *return_len = x_count + 1;
    
    int index = 0;
    for(int i = 0; i < len; i++){
        if(myString[i] == 'x') {
            index++;
        }
        else {
            answer[index]++;
        }
    }
    
    return answer;
}