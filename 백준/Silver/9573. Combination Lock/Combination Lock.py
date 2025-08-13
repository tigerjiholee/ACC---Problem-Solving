import sys; input = sys.stdin.readline

n = int(input())
J = list(map(int, input().split(" ")))
M = list(map(int, input().split(" ")))

tmp = [_ for _ in range(1, n+1)] 
j = [list((J[i]+x-1)%n for x in range(-2,3)) for i in range(3)]
m = [list((M[i]+x-1)%n for x in range(-2,3)) for i in range(3)]

ans = 2 * min(5,n)**3
count = 1
for i in range(3):
    count *= len(set(j[i]).intersection(set(m[i])))

print(ans-count)