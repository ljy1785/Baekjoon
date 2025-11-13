n = int(input())
data = list(map(int, input().split()))
max = max(data)
modified = []
for i in data:
  modified.append(i/max*100)

print(sum(modified)/len(modified))