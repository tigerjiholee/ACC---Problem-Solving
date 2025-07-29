import sys; input = sys.stdin.readline

n = int(input())
if (n-1)%4 == 0 or (n-3)%4 == 0:
    print("SK")
else:
    print("CY")