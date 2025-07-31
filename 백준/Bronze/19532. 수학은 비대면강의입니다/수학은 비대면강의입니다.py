ans = []
a, b, c, d, e, f = map(int, input().split(" "))
for x in range(-999, 1000): 
  if ans != []:
    break
  else: 
    for y in range(-999, 1000):
      if a*x+b*y == c and d*x + e*y == f: 
        ans.append((x,y))
        break
print(ans[0][0], ans[0][1])