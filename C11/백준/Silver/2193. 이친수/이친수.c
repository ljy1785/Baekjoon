#include <stdio.h>

int main() {
    int n;
    long long dp[91];

    scanf("%d", &n);
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    dp[4] = 3;
    for (int i = 5; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    printf("%lld\n", dp[n]);
    return 0;
}