import sys; input = sys.stdin.readline
import itertools

n = int(input())
cows = sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"])
Const = [list(input().strip().split(" must be milked beside ")) for _ in range(n)]

P = list(itertools.permutations(cows,8)) 

for item in P: 
  check = True 
  for i in Const: 
    if abs(item.index(i[0]) - item.index(i[1])) > 1: 
      check = False 
      break

  if check: 
    print(*item, sep = "\n") 
    break