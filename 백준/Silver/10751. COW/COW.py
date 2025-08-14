n = int(input())
T = list(input().strip())

c = 0
co = 0
ans = 0
for let in T: 
  if let == "C": 
    c += 1
  elif let == "O": 
    co += c
  else: 
    ans += co

print(ans)