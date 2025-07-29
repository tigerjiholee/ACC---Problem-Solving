import sys; input = sys.stdin.readline

string = input().strip()
n = int(input())
rings = []
for i in range(n):
    rings.append(input().strip()*2)

count = 0
for ring in rings:
    for i in range(len(ring)-len(string)):
        if ring[i:i+len(string)] == string:
            count += 1
            break

print(count)