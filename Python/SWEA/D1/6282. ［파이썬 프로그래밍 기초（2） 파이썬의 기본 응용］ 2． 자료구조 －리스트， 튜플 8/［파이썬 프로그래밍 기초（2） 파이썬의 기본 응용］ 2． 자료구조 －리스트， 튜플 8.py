numbers = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
filtered = list(filter(lambda x : x % 2 == 0, numbers))
print(filtered)