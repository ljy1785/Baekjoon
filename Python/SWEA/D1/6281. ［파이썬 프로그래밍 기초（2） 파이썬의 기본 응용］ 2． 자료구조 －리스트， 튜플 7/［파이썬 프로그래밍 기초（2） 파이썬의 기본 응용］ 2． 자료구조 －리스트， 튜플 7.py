n = int(input())
numbers = [i for i in range(1, n+1) if n % i == 0]
print(numbers)
