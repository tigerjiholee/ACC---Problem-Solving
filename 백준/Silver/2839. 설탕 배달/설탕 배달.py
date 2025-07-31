n = int(input())
ans = -1
for a in range(n//5, -1, -1):
  if (n-5*a)%3 == 0:
    ans = a + (n-5*a)//3
    break
print(ans)