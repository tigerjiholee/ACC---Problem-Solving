n, k = map(int, input().split(" "))
li = []
for i in range(n):
  li.append(int(input()))
li.sort()

ans = []
for i in range(n): 
  count = 0
  for j in range(i, n):
    if li[j] <= li[i]+k: 
      count += 1
  ans.append(count)

print(max(ans))