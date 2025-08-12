n = int(input())
li = []
for i in range(n): 
  li.append(int(input()))

ans = 0
for i in range(n): 
  if li[i] != sorted(li)[i]: 
    ans += 1
if ans == 0: 
  print(0)
else: 
  print(ans-1) 