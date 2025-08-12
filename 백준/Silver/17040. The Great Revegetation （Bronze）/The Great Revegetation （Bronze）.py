n, m = map(int, input().split(" "))
li = [ [] for _ in range(n+1)]
for i in range(m): 
  a, b = map(int, input().split(" "))
  li[a].append(b)
  li[b].append(a)

# [[], [4, 2, 5], [4, 5, 1], [4], [1, 2, 3], [2, 1]] 

ans =  [0] * (n+1)  
for i in range(1,n+1): 
  t = [5,1,2,3,4]
  for j in li[i]: 
    if ans[j] != 0: 
      t[ans[j]] = 5
  ans[i] = min(t)



print(*ans[1:n+1],sep="")