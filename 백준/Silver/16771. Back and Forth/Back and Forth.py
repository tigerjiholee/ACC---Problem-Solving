B1 = list(map(int, input().split(" ")))
B2 = list(map(int, input().split(" ")))
ans = {0}

for a in B1 : 
  for b in B2 : 
    ans.add(-a + b)

for a in range(10) : 
  for b in range(10) : 
    for c in range(10) : 
      for d in range(10) : 
        if (a != c) and ( b != d ) : 
          ans.add(-B1[a] + B2[b] -B1[c] + B2[d])

print(len(ans))