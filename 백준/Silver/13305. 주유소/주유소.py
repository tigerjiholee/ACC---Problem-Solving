n = int(input())
D = list(map(int, input().split(" ")))
P = list(map(int, input().split(" ")))

s = D[0]*P[0]
min_p = P[0]

for i in range(1, n-1): 
  if P[i] < min_p:
    min_p = P[i]
  s += D[i]*min_p

print(s)