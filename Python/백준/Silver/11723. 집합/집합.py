import sys
n = int(sys.stdin.readline())
S = set()

for _ in range(n):
  line = sys.stdin.readline().split()
  ins = line[0]
  
  
  if(ins=='add'): S.add(int(line[1]))
  elif(ins=='remove'):  S.discard(int(line[1]))
  elif(ins=='check'):
    print(1 if int(line[1]) in S else 0)
  elif(ins=='toggle'):
    if int(line[1]) in S: S.discard(int(line[1]))
    else : S.add(int(line[1]))
  elif(ins=='all'): S = set(range(1, 21))
  else: S = set()