n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

num_list = [0]*200
for element in segments:
    A = element[0]
    B = element[1]
    for i in range(A+100, B+100):
        num_list[i] += 1 

print(max(num_list))