t = int(input())
for i in range(t):
  n = int(input())
  item = list(map(int,input().split()))
  ans = 0
  total = sum(item)
  for i in range(n ,0,-1):
    if total%i == 0: 
      target = total//i
      s = 0
      sign = True 
      for j in range(n):
        s += item[j]
        if (s > target) : 
          sign = False 
          break 
          
        if s == target:
          s = 0

      if (sign) : 
        print(n-i)
        break 