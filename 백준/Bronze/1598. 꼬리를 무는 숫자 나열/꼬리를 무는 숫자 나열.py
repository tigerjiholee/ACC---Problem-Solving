import sys; input = sys.stdin.readline

a, b = map(int, input().split(" "))
if a%4 == 0:
  x = 4
else:
  x = a%4
if b%4 == 0: 
  y = 4
else: 
  y = b%4
v = abs(x-y)
h = abs((a-1)//4 - (b-1)//4)
print(v+h)