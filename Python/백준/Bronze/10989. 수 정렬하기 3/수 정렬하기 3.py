import sys
n = int(input())
def input():
    return sys.stdin.readline()
count = [0] * 10001
for i in range(n):
    num = int(input())
    count[num] += 1
   
for number in range(1, 10001):
    if count[number] != 0:
        for j in range(count[number]):
            print(number)