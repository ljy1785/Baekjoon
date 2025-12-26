n = int(input())
dot_list = []
for i in range(n):
  x, y = input().split()
  dot_list.append((int(x), int(y)))
dot_list.sort()
for x, y in dot_list:
  print(x, y)