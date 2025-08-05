n = int(input())
s = input()

for k in range(1,n+1): 
  if len(set(s[i:i+k] for i in range(n-k+1))) == (n-k+1)  :
    print(k)
    break