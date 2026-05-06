#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int* solution(int arr[], size_t arr_len, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*k);
    for (int i = 0; i < k; i++) answer[i] = -1;
    bool* checked = (bool*)calloc(10001, sizeof(bool));
    int count = 0;
    for (int i = 0; i < arr_len; i++){
        int current = arr[i];
        if(!checked[current]){
            checked[current] = true;
            answer[count] = current;
            count++;
        }
        if(count == k) break;
    }
    free(checked);
    return answer;
}