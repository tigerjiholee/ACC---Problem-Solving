n = int(input())
log = list(map(int, input().split(" ")))
m,M = 0,0

log[0] = 0

for i in range(n): 
  if log[i] != -1: 
    for j in range(1,log[i]+1):
      if log[i-j] != -1 and log[i-j] != log[i]-j: 
        print(-1)
        exit()
      log[i-j] = log[i]-j


m = len(list(x for x in log if x==0))
M = len(list(x for x in log if x==0 or x==-1))

print(m, M)