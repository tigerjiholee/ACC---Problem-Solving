import sys; input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

ans = []
for door in range(n): #0,1,2,3,4
    d = 0
    for room in range(n):
        d += li[room]*((room-door) if room-door>=0 else (n-door+room))
    ans.append(d)

print(min(ans))