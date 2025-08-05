import sys; input = sys.stdin.readline
import itertools

n = int(input().strip()) 
a, b = map(int, input().strip().split(" ")) 
c = int(input().strip()) 
D = []
for i in range(n):
    D.append(int(input()))
D.sort()

P = [a+b*k for k in range(0,n+1)]
C = [c+sum(D[n-k:]) for k in range(0,n+1)]

print(max(C[i]//P[i] for i in range(len(P))))