import sys
n = int(input())
member_list = []
for i in range(n):
  age, name = input().split()
  member_list.append([int(age), str(name)])

member_list.sort(key = lambda x : x[0])
for age, name in member_list:
  print(age, name)