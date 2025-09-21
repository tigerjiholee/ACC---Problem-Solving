ans = [list(input()) for _ in range(3)]
guess = [list(input()) for _ in range(3)]
g,y = 0,0


for i in range(3): 
  for j in range(3): 
    if guess[i][j] == ans[i][j]: 
      g += 1
      guess[i][j] = ""
      ans[i][j] = ""

for i in range(3): 
  for j in range(3): 
    for q in range(3) : 
      for w in range(3): 
        if (guess[i][j] == ans[q][w]) and (guess[i][j] != ""): 
          y += 1 
          guess[i][j] = ""
          ans[q][w] = ""
          break 

print(g)
print(y)