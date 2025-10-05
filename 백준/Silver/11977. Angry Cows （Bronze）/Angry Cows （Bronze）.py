n = int(input())
li = sorted(list(int(input()) for i in range(n)))

def f(start,direction): 
  prev = start 
  r = 1 
  while 0 <= prev < n : 
    next = prev
    while (0 <= next + direction < n) and ( abs(li[next+direction] - li[prev]) <= r  )  : 
      next += direction

    if next == prev : break 
    prev = next 
    r += 1 
  return prev 
    

ans = []
for b in range(n): 
  left = f(b,-1) 
  right = f(b,1) 
  ans.append(right-left+1)
print(max(ans))