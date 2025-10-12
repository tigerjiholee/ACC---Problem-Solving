k,n = map(int,input().split(" "))
M = input().strip().split(" ")
pos = {} 
for i in range(n) : 
  pos[M[i]] = i 

grid = [[("B" if i==j else "?") for j in range(n)] for i in range(n)]

for i in range(k) : 
  author = input().split() 
  for j in range(n) : 
    check = False 
    for l in range(j+1,n) : 
      if author[l-1] > author[l] : check = True
      if check: 
        grid[pos[author[l]]][pos[author[j]]] = 1 
        grid[pos[author[j]]][pos[author[l]]] = 0 

for i in range(n): 
  for j in range(n): 
    print(grid[i][j], end="")
  print()