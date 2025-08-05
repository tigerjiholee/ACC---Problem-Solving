import sys; input = sys.stdin.readline

n = int(input())
log = []
for i in range(n):
    day, cow, delta = input().strip().split(" ")
    log.append((int(day), cow, delta[0], int(delta[1:])))
log.sort()

count = 0
I = {"Bessie":7, "Elsie":7, "Mildred":7}
for day in log:
    tmp = dict(I)
    tmp[day[1]] += day[3] if day[2]=="+" else -day[3]
    
    if sorted([k for k,v in I.items() if v==max(I.values())]) != sorted([k for k,v in tmp.items() if v==max(tmp.values())]): 
        count += 1
    I = dict(tmp)

print(count)