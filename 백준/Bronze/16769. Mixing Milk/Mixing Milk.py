C = []
M = []
for i in range(3): 
  c,m = map(int,input().split(" "))
  C.append(c)
  M.append(m)

for i in range(100): 
  s = 0 if M[i%3]+M[(i+1)%3] <= C[(i+1)%3] else M[i%3]+M[(i+1)%3]-C[(i+1)%3]
  t = C[(i+1)%3] if M[i%3]+M[(i+1)%3] > C[(i+1)%3] else M[i%3]+M[(i+1)%3]
  M[i%3],M[(i+1)%3] = s,t

for i in range(3): 
  print(M[i])