n = int(input())
F = [-1]
for i in range(n): 
  F.append(int(input()))

ans = 0
for i in range(1,n+1): 
  t = i
  tmp = {t}
  while True: 
    if F[t] == 0: 
      ans += 1
      break
    elif F[t] in tmp: 
      break
    else: 
      t = F[t]
      tmp.add(t)
print(ans)