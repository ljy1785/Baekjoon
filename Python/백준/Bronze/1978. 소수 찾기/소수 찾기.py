n = int(input())
data = list(map(int,input().split()))

def is_prime(x):
  if x <= 1: 
    return False
  if x == 2:
    return True
  if x % 2 == 0:
    return False
  limit = int(x**0.5)
  for d in range(3, limit+1, 2):
    if x % d == 0:
       return False
  return True

count = 0
for i in data:
  if is_prime(i) == True:
    count += 1

print(count)