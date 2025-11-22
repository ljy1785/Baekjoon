numbers = [i for i in range(1, 11)]
filtered = list(filter(lambda x : x % 2 == 0, numbers))
print(filtered)