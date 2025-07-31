import sys; input = sys.stdin.readline

eq = list(input().strip().split("-"))

tot = 0
for i in range(len(eq)):
    tmp = sum(list(map(int, eq[i].split("+"))))
    if i == 0:
        tot += tmp
    else:
        tot -= tmp

print(tot)