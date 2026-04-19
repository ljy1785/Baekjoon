import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
  
dp = a[:]

for i in range(1, n):
  for j in range(i):
    if a[j] < a[i]: dp[i] = max(dp[i], dp[j] +a[i])

print(max(dp))