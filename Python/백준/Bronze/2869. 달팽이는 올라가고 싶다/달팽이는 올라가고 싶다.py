A, B, V = map(int, input().split())
quo = int((V-A) //(A-B))
rem = (V-A) % (A-B)
answer = 0
if rem == 0 : answer = quo + 1
else : answer = quo + 2
print(answer)