import sys

n = int(sys.stdin.readline())
words = {sys.stdin.readline().strip() for _ in range(n)}  # 중복 제거

for w in sorted(words, key=lambda x: (len(x), x)):  # 길이 → 사전순
    print(w)
