result = []
def checking(tomato):
  check = True
  for i in range(len(tomato)//2):
    if tomato[i] != tomato[-i-1] : 
      check = False
      break
  if check: result.append('yes')
  else: result.append('no')

while(1):
  tomato = str(input())
  if tomato == '0': break
  checking(tomato)

for i in result:
  print(i)