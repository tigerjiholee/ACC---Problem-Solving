a, b, n = map(int, input().split(" "))
R = []
for i in range(n): 
  c, t = map(int, input().split(" "))
  R.append([c, list(map(int, input().split(" ")))])

C = []
for r in R: 
  if a in r[1]: 
    for i in r[1][r[1].index(a):]: 
      if i == b: 
        C.append(r[0])
if C == []: 
  print(-1)
else: 
  print(min(C))