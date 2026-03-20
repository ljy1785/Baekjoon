import sys
n = int(input())
numbers = [sys.stdin.readline().strip() for _ in range(n)]

for number in sorted(numbers, key = int):
    print(number)
