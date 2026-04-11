#include <stdio.h>
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
int st[2][100001];
int dp[2][100001];

int main() {
    int n, t;

    scanf("%d", &t);
    
    while(t--){
        scanf("%d", &n);
        for (int i = 0; i<n ; i++){
            scanf("%d", &st[0][i]);
        }
        for (int i = 0; i<n ; i++){
            scanf("%d", &st[1][i]);
        }
        
        dp[0][0] = st[0][0];
        dp[1][0] = st[1][0];

        if(n>1){
            dp[0][1] = st[1][0] + st[0][1];
            dp[1][1] = st[0][0] + st[1][1];
        }
        for(int i = 2; i<n; i++){
            dp[0][i] = MAX(dp[1][i - 1], dp[1][i - 2]) + st[0][i];
            dp[1][i] = MAX(dp[0][i - 1], dp[0][i - 2]) + st[1][i];
        }
        
        printf("%d\n", MAX(dp[0][n - 1], dp[1][n - 1]));    
    }
    return 0;
}