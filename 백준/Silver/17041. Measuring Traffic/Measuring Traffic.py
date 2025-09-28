n = int(input())
log = []
for i in range(n):
  tmp = input().split()
  log.append([tmp[0], int(tmp[1]), int(tmp[2])])

l, h = 0, float("inf")
for i in range(n - 1, -1, -1):
  if log[i][0] == "none":
    l = max(l, log[i][1])
    h = min(h, log[i][2])
  elif log[i][0] == "on":
    l -= log[i][2] 
    h -= log[i][1]
    l = max(0,l)
  elif log[i][0] == "off":
    l += log[i][1]
    h += log[i][2]
print(l, h)

l, h = 0, float("inf")
for i in range(n):
  if log[i][0] == "none":
    l = max(l, log[i][1])
    h = min(h, log[i][2])
  elif log[i][0] == "on":
    l += log[i][1]
    h += log[i][2]
  elif log[i][0] == "off":
    l -= log[i][2]
    h -= log[i][1]
    l = max(0,l)
print(l, h)