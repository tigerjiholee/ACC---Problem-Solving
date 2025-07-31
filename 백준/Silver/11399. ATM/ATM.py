n = int(input())
P = list(map(int, input().split(" ")))
P.sort()

print(sum(P[i]*(n-i) for i in range(0,n)))