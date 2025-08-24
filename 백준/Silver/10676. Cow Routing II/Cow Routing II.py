import sys; input = sys.stdin.readline


A,B,N = map(int,input().split())
costs = [] 
routes = []
ans = float("inf")
for i in range(N): 
    c,r = map(int,input().split())
    costs.append([c,r])
    routes.append(list(map(int,input().split())))
    start,end = False,False 
    for j in range(r):
       if routes[i][j] == A : start = True
       elif routes[i][j] == B and start  : end = True 
    if end : ans = min(ans,c)

for i in range(N) : 
    for j in range(N) : 
        if (i == j) or (costs[i][0] + costs[j][0] > ans) : continue
        start, trans, end = -1,-1,-1
        for x in range(costs[i][1]) : 
            if routes[i][x] == A : 
                start = i
            if start != -1 : 
                t = routes[i][x] 
                for y in range(costs[j][1]) : 
                    if routes[j][y] == t : 
                        trans = t 
                    if trans != -1 and routes[j][y] == B : 
                        ans = min(ans, costs[i][0] + costs[j][0])
                        end = y

                if end == -1 : 
                    trans = -1
                else : 
                    break 

if ans == float("inf") : print(-1) 
else : print(ans)