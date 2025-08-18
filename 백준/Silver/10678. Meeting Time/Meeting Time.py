import sys; input = sys.stdin.readline

def dfs(r,t,c): 
    if r == n: 
        if c == 0: 
            bt.append(t)
        else: 
            et.append(t)
        return
    for item in li[r]: 
        if c == 0: 
            dfs(item[0], t+item[1], c)
        else: 
            dfs(item[0], t+item[2], c)
    return

n, m = map(int, input().split(" "))
li = [[] for _ in range(n+1)]

for i in range(m): 
  a, b, c, d = map(int, input().split(" "))
  li[a].append([b,c,d])

bt = []
et = []

dfs(1,0,0)
dfs(1,0,1)

if len(set(bt).intersection(set(et))) == 0: 
    print("IMPOSSIBLE")
else:
    print(min(set(bt).intersection(set(et))))