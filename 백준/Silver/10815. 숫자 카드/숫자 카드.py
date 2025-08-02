import sys; input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(" ")))
nums.sort()
m = int(input())
tnums = list(map(int, input().split(" ")))

ans = []
for tnum in tnums:
    l, r = 0, n-1
    check = False
    while l <= r: 
        if tnum > nums[(l+r)//2]: 
            l = (l+r)//2 + 1
        elif tnum < nums[(l+r)//2]: 
            r = (l+r)//2 - 1
        else:
            check = True
            break
    ans.append(1) if check == True else ans.append(0)

for num in ans:
    print(num, end=" ")