N,M = map(int,input().split())
basket = [ n for n in range(1,N+1) ]

for m in range(M):
    i,j =  map(int,input().split())
    for n in range(i-1,(j+i)//2):
        basket[n],basket[j-1-n+i-1] = basket[j-1-n+i-1], basket[n]
      
print(*basket) 