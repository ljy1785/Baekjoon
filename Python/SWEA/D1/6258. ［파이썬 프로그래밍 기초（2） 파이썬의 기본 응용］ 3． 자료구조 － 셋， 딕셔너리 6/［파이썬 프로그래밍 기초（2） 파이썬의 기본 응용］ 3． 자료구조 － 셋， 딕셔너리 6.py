n = int(input())
print(dict(map(lambda x: (x, x**2), range(1, n+1))))