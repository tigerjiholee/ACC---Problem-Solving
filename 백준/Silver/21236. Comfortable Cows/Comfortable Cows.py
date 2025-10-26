def check(x,y):
  if grid[x][y] == 0 : return False 
  count = 0
  for i in range(4):
    if 0<= x+dx[i] <= mx and 0<=y+dy[i]<= my and grid[x+dx[i]][y+dy[i]] == 1:
      count += 1
  return count == 3

n = int(input())
li = []
mx,my = 0,0
for i in range(n):
  x,y = map(int,input().split())
  li.append((x,y))
  if x > mx: 
    mx = x
  if y > my:
    my = y

grid = [[0 for _ in range(my+1)] for _ in range(mx+1)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

count = 0
 
for pair in li: 
  for i in range(4):
    if (0 <= pair[0] + dx[i] <= mx ) and (0<=pair[1]+dy[i]<=my) and check(pair[0]+dx[i],pair[1]+dy[i]):
      count -= 1
  
  grid[pair[0]][pair[1]] = 1
  if check(pair[0],pair[1]):
    count += 1
    
  for i in range(4):
    if (0 <= pair[0] + dx[i] <= mx ) and (0<=pair[1]+dy[i]<=my) and check(pair[0]+dx[i],pair[1]+dy[i]):
      count += 1
  print(count)