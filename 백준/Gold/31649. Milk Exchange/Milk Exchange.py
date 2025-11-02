n,m = map(int,input().split())
S = list(input())
A = list(map(int,input().split()))

ans = sum(A)
for i in range(n): 
  if (S[i] == "R") and (S[ (i+1) % n] == "L") : 
    tmp = 0 
    j = (i-1+n) % n
    while (S[j] == "R") : 
      tmp += A[j]
      j = (j-1+n) % n
    ans -= min(m,tmp) 

  if (S[i] == "L") and (S[(i-1+n) % n] == "R") : 
    tmp = 0
    j = (i+1)%n
    while S[j] == "L":
      tmp += A[j]
      j = (j+1)%n
    ans -= min(m,tmp)

    
print(ans)