#include <stdio.h>
int max(int a, int b, int c){
  int res = a;
  if (b > res) res = b;
  if (c > res) res = c;
  return res;
}

int main(){
  int n;
  int a, b, c;
  int amount[10001];
  int dp[10001];
  
  scanf("%d", &n);
  for (int i = 1; i<=n;i++){
    scanf("%d", &amount[i]);
  }
  
  dp[0] = 0;
  dp[1] = amount[1];
  if (n >= 2) dp[2] = amount[1] + amount[2];
    
  for (int i = 3; i<=n; i++){
    a = dp[i-1];
    b = dp[i-2] + amount[i];
    c = dp[i-3] + amount[i-1] + amount[i];
    dp[i] = max(a, b, c);
  }
  printf("%d\n", dp[n]);
  return 0;
}