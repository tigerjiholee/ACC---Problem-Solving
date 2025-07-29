import sys; input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
  a, b = map(int, input().split(" "))
  li.append((a,b))

grid = [[0 for i in range(100)] for j in range(100)]
for item in li:
  for i in range(item[0], item[0]+10):
    for j in range(item[1], item[1]+10):
      grid[i][j] = 1

count = 0
for row in grid:
  for num in row:
    if num == 1:
      count += 1

print(count)