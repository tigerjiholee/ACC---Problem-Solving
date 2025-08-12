n = int(input())
li = [list(input().strip()) for _ in range(n)]

ans = 0
i, j = n-1, n-1
check = [ ['0' for _ in range(n)] for _ in range(n)]

while li != check : 
  if li[i][j] == "1": 
    ans += 1
    for row in range(i+1): 
      for col in range(j+1): 
        li[row][col] = "1" if li[row][col] == "0" else "0"
  if j == 0: 
      i -= 1
      j = n-1 
  else:
      j -= 1
    

print(ans)