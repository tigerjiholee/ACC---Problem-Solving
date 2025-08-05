import sys; input = sys.stdin.readline

n = int(input()) 
count = 0
cow_stat = {}
for i in range(n):
    a, b = map(int, input().strip().split(" "))
    if a in cow_stat.keys() and b != cow_stat[a]: 
        count += 1
    cow_stat[a] = b 

print(count)