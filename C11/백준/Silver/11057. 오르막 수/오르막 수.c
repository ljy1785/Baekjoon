#include <stdio.h>

int main() {
    int n;
    int result = 0;
    int dp[1001][10] = {0,};

    scanf("%d", &n);
    for (int i = 0; i <= 9; i++) {
        dp[1][i] = 1;
    }

    for (int i = 2; i <= n; i++) {
        for (int j = 0; j <= 9; j++) {
            if (j == 0) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10007;
            }
        }
    }

    for (int i = 0; i <= 9; i++) {
        result = (result + dp[n][i]) % 10007;
    }

    printf("%d\n", result);
    return 0;
}