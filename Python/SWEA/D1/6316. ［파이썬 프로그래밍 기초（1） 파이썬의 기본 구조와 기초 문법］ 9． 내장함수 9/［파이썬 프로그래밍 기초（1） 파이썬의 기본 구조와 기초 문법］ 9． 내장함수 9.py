#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for num in filter(lambda x: x % 2 == 0, range(1, 11)):
	even.append(num)
    
print(list(map(lambda x : x **2, even)))