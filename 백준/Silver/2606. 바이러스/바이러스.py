import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

n = int(input())
m = int(input())
li = [[] for _ in range(n+1)]
for i in range(m): 
  a, b = map(int, input().split(" "))
  li[a].append(b)
  li[b].append(a)

S = [0] * (n+1)
def dfs(x): 
  S[x] = 1
  for y in li[x]: 
    if S[y] == 0: 
      dfs(y)

dfs(1)
print(sum(S)-1)