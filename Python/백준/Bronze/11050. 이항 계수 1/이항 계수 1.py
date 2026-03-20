n, k = map(int,input().split())
numerator, denominator = 1, 1
for i in range(1, k+1):
  denominator *= i
for j in range(n-k+1, n+1):
  numerator *= j
print(int(numerator/denominator))