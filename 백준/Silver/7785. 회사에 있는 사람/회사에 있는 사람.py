S = set() 

n = int(input())
for i in range(n):
  a, b = input().strip().split(" ")
  if b == "enter":
    S.add(a)
  else:
    S.remove(a)

S = sorted(S, reverse=True)
for name in S:
  print(name)