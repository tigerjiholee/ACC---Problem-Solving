n = int(input())
li = []
for i in range(n):
  x,y = map(int, input().split(" "))
  li.append((x,y))

xmin,xmin2,xmax,xmax2 = 40000,0,0,0
ymin,ymin2,ymax,ymax2 = 40000,0,0,0

for item in li: 
  if item[0] > xmax: 
    xmax2 = xmax
    xmax = item[0]
  elif item[0] > xmax2: 
    xmax2 = item[0]
  if item[0] < xmin: 
    xmin2 = xmin
    xmin = item[0]
  elif item[0] < xmin2: 
    xmin2 = item[0]
  if item[1] > ymax: 
    ymax2 = ymax
    ymax = item[1]
  elif item[1] > ymax2: 
    ymax2 = item[1]
  if item[1] < ymin: 
    ymin2 = ymin
    ymin = item[1]
  elif item[1] < ymin2: 
    ymin2 = item[1]

ans = (xmax-xmin) * (ymax-ymin)

for x,y in li: 
  tmaxx,tminx = xmax,xmin
  tmaxy,tminy = ymax,ymin

  if x == tminx : tminx = xmin2
  if x == tmaxx : tmaxx = xmax2 
  if y == tminy : tminy = ymin2
  if y == tmaxy : tmaxy = ymax2 
  
  ans = min(ans, (tmaxx-tminx ) * (tmaxy-tminy))

print(ans)