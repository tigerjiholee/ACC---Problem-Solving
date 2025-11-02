x,y = map(int,input().split())

ans = 0 
for d in range(len(str(x)),len(str(y))+1):
  for i in range(10):
    s = [str(i)] * d
    for j in range(10) : 
      if i == j : continue
      for k in range(d) : 
        s[k] = str(j) 
        interesting = "".join(s)
        if (s[0] != '0') and (x<=int(interesting)<=y) : 
          ans += 1 
        s[k] = str(i) 
print(ans)