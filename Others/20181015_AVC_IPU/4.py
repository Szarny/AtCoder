N = int(input())
A = list(map(int,input().split()))
Acount = {}
q = []
 
for a in A:
  if a not in Acount:
    Acount[a] = 0
  
  Acount[a] += 1
    
for key, val in Acount.items():
  if val >= 2:
    q.append(key)
    
  if val >= 4:
    q.append(key)
 
q.sort(reverse=True)
 
if len(q) < 2:
  print(0)
else:
  print(q[0]*q[1])
