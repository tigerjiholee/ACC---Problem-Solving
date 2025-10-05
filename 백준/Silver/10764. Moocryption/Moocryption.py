n,m = map(int,input().split(" "))
grid = [ input()  for i in range(n)]
dx = [1,1,0,-1,-1,-1,0, 1] 
dy = [0,-1,-1,-1, 0,1,1,1] 
ans = {} 

for i in range(n) : 
  for j in range(m) : 
    for k in range(8) : 
      if 0 <= i + dy[k] * 2 < n and 0 <= j + dx[k] * 2 < m : 
        if grid[i][j] != "M" and grid[i][j] != grid[i+dy[k]][j+dx[k]] == grid[i+dy[k]*2][j+dx[k]*2]  != "O" : 
          target = grid[i][j] + grid[i+dy[k]][j+dx[k]] + grid[i+dy[k]*2][j+dx[k]*2] 
          ans[target] = ans.get(target,0) + 1 
        

if len(ans) > 0 : 
  print(max(ans.values())) 
else : 
  print(0)