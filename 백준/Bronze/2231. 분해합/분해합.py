n = int(input())
ans = 0
for i in range(1, n+1):
  D = list(str(i))
  s = 0
  for num in D: 
    s += int(num)
  if i+s == n:
    ans = i
    break
print(ans)