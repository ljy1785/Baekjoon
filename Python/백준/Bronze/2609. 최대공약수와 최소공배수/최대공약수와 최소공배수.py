import math

N, K = map(int, input().split())
def lcm(a, b) :
  return a*b//math.gcd(a, b)
print(math.gcd(N, K))
print(lcm(N, K))