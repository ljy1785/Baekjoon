def exponential(num, divider):
    count = 0
    while num % divider == 0:
        count += 1
        num //= divider
    return count

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    a = exponential(N, 2)
    b = exponential(N, 3)
    c = exponential(N, 5)
    d = exponential(N, 7)
    e = exponential(N, 11)

    print(f"#{t} {a} {b} {c} {d} {e}")