import sys; input = sys.stdin.readline

n = int(input())
E = sorted([int(input()) for _ in range(n)])
B = sorted(list(set([_ for _ in range(1, 2*n+1)]) - set(E)))

score = 0
b = 0
e = 0
while e < n and b < n: 
  if B[b] > E[e]:
    score += 1
    e += 1
    b += 1 
  else: 
    b += 1
print(score)