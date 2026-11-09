n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

num_list = list(0 for _ in range(n+1))
for element in commands:
    A = element[0]
    B = element[1]
    for i in range(A, B+1):
        num_list[i] += 1



print(max(num_list))