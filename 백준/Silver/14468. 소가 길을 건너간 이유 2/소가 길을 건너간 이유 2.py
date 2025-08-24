log = input()

ans = 0
for i in set(log): 
  tmp = []
  for j in range(log.index(i)+1,52): 
    if log[j] == i: 
      ans += len(tmp)
      break
    elif log[j] in tmp: 
      tmp.remove(log[j])
    else:
      tmp.append(log[j])
print(ans//2)