n = int(input())
L = []
G = []
for i in range(n): 
  a,b = input().split(" ")
  if a == "G": 
    G.append(int(b))
  else: 
    L.append(int(b))

G.sort() 
L.sort() 

ans = float("inf")
j = 0 
for i in range(len(G)+1):
  if i == 0 : maxG = float("-inf")
  else : maxG = G[i-1]

  while j < len(L) and L[j] < maxG : 
    j += 1 

  removed = (len(G) - i) + j

  if removed < ans : 
    ans = removed 
  
print(ans)