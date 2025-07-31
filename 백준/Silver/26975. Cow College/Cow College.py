import sys; input = sys.stdin.readline

n = int(input())
C = list(map(int, input().split(" ")))
C.sort()

max_p = 0
opt_t = []

for i in range(n):
    if C[i]*(n-i) > max_p:
        max_p = C[i]*(n-i)
        opt_t = C[i]
    elif C[i]*(n-i) == max_p:
        opt_t = min(C[i], opt_t)

print(max_p, opt_t)