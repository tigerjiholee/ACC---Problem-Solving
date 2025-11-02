import sys; input = sys.stdin.readline

n,q = map(int,input().split())
li = []
for i in range(q):
  li.append(tuple(map(int,input().split())))

xy = dict()
yz = dict()
za = dict()

cnt = 0
for i in range(q):
  cur = li[i]
  xy[(cur[0],cur[1])] = xy.get((cur[0],cur[1]),0) + 1
  yz[(cur[1],cur[2])] = yz.get((cur[1],cur[2]),0) + 1
  za[(cur[2],cur[0])] = za.get((cur[2],cur[0]),0) + 1
  if xy[(cur[0],cur[1])] == n: 
    cnt += 1
  if yz[(cur[1],cur[2])] == n: 
    cnt += 1
  if za[(cur[2],cur[0])] == n: 
    cnt += 1
  print(cnt)