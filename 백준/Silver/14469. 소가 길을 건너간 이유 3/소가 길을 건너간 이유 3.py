n = int(input())
C = []
for i in range(n):
  C.append(list(map(int, input().split(" "))))
C.sort()

time = 0
for i in range(n): 
  if C[i][0] > time  : 
    time = C[i][0] + C[i][1]
  else : 
    time += C[i][1] 

print(time) 