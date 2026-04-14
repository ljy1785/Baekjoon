import sys
n, m = map(int, sys.stdin.readline().split())
not_listened = set()
not_seen = set()
for _ in range(n):
  name = sys.stdin.readline().strip()
  not_listened.add(name)
for _ in range(m):
  name = sys.stdin.readline().strip()
  not_seen.add(name)

both_not = not_listened & not_seen
result = sorted(list(both_not))

print(len(result))
for name in result:
  print(name)