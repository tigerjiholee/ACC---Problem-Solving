import sys; input = sys.stdin.readline

N, M, D, S = map(int, input().split(" "))
transcript = {}
sick = {}

for i in range(D): 
    p, m, t = map(int, input().split(" "))
    if p not in transcript.keys(): 
        transcript[p] = [(m,t)]
    else: 
        transcript[p].append((m,t))

for i in range(S): 
    p, t = map(int, input().split(" "))
    sick[p] = t

sm = set(_ for _ in range(1, M+1))
for k,v in sick.items(): 
    tmp = set(i[0] for i in transcript[k] if i[1]<v)
    sm = sm.intersection(tmp)

ans = 0
for milk in sm: 
    count = 0
    for v in transcript.values(): 
        tmp = set(x[0] for x in v)
        count += 1 if milk in tmp else 0
    ans = max(ans, count)

print(ans)