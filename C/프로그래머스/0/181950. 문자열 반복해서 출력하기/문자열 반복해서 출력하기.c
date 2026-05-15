#include <stdio.h>
#define LEN_INPUT 11

int main(void) {
    char s1[LEN_INPUT];
    int a;

    // 문자열과 정수를 입력받음
    if (scanf("%s %d", s1, &a) != 2) return 0;

    // a번 반복하여 s1을 출력
    for (int i = 0; i < a; i++) {
        printf("%s", s1);
    }

    return 0;
}