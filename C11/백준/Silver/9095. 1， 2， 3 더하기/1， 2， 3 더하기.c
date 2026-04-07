#include <stdio.h>

int main(){
  int count;
  int n;
  int dp[12];
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;
  for (int i = 4; i <=10; i++){
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
  }
  scanf("%d", &count);
  for (int i = 0; i<count; i++){
    scanf("%d", &n);
    printf("%d\n", dp[n]);
  }
  
  return 0;
}