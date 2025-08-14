import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

n, m, r = map(int, input().split(" "))
li = [[] for _ in range(n+1)]
for i in range(m): 
  u, v = map(int, input().split(" "))
  li[u].append(v)
  li[v].append(u)

visited = [0] * (n+1)
cnt = 1 
def dfs(r): 
  global cnt
  visited[r] = cnt
  cnt += 1 
  for x in sorted(li[r], reverse=True): 
    if visited[x] == 0: 
      dfs(x)
dfs(r)

for i in range(1,n+1): 
  print(visited[i])