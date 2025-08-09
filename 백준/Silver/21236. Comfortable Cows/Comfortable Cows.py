def isValid(x,y) : 
  return 0 <= x <= 1000 and 0 <= y <= 1000

def check(x,y): 
  if grid[x][y] == 0:
    return 0 
  res = 0 
  for dir in dirs[1:]: 
    if isValid(x+dir[0], y+dir[1]) and grid[x+dir[0]][y+dir[1]]: 
      res += 1 
  return res == 3 

n = int(input())
grid = [[0] * 1001 for _ in range(1001)] 
dirs = [[0,0], [-1,0], [1,0], [0,-1], [0,1]]

comf = [[0] * 1001 for _ in range(1001)] 
ans = []
an = 0
for i in range(n): 
  x,y = map(int,input().split())
  grid[x][y] = 1
  
  for dir in dirs:
    nx, ny = x+dir[0], y+dir[1]
    if isValid(nx,ny): 
      if check(nx, ny) and not comf[nx][ny]: 
        an += 1
        comf[nx][ny] = 1
      elif not check(nx, ny) and comf[nx][ny]: 
        an -= 1
        comf[nx][ny] = 0

  ans.append(an)

for item in ans:
  print(item)