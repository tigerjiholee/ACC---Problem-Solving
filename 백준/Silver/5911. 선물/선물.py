n, b = map(int, input().split(" "))
li = []
for i in range(n): 
  p, s = map(int, input().split(" "))
  li.append((p,s))

mx = 0
for i in range(n): 
  tmp = [] 
  for j in range(n): 
    if j == i: 
      tmp.append(li[j][0]//2 + li[j][1]) 
    else:
      tmp.append(li[j][0] + li[j][1])
  tmp.sort()
  count = 0
  s = 0
  for item in tmp: 
    s += item
    if s > b: 
      break
    count += 1
  if count > mx: 
    mx = count

print(mx)