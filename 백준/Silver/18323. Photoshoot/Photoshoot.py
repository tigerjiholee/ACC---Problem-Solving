n = int(input())
B = list(map(int, input().split(" ")))

for i in range(1,n+1): 
  ans = [i]
  for j in range(1,n): 
      tmp = B[j-1] - ans[j-1]
      if (tmp in ans) or  (tmp <= 0) : 
        break 
      ans.append(B[j-1] - ans[j-1])
    
  if len(ans) == n : 
    print(*ans)
    break 