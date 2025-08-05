n = int(input())
li = list(map(int, input().split(" ")))
e,o = 0,0
for i in range(n):
  if li[i]%2 == 0:
    e += 1
  else:
    o += 1

while o > e:
  o -= 2
  e += 1

if o==e:
  print(2*o)
else:
  print(2*o+1)