n = int(input())
result = []
for i in range(1, n+1):
  data = []
  data = list(map(int, input().split()))
  result.append(data[0]+data[1])
for j in result:
  print(j)
