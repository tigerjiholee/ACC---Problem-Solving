n = int(input())
D = list(map(int, input().split(" ")))
P = list(map(int, input().split(" ")))

s = D[0]*P[0]
for i in range(1, n):
  if P[i] == min(p for p in P[:n-1]):
    s += P[i]*sum(d for d in D[i:])
    break
  else: 
    s += P[i]*D[i]
print(s)