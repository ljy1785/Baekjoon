n, m = map(int,input().split())
numbers = list(map(int, input().split()))
answer = 0
for i in numbers:
  for j in numbers:
    for k in numbers:
      if (i != j) & (j != k) & (i != k):
        sum = i + j + k
        if (sum <= m) & (sum > answer): answer = sum

print(answer)