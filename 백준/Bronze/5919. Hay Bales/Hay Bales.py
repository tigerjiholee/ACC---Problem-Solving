n = int(input())
li = []
for i in range(n): 
    li.append(int(input()))

ans = 0
for item in li: 
    ans += abs(item-sum(li)//n)
print(ans//2)