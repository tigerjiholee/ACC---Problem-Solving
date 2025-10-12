import sys;input = sys.stdin.readline
import itertools

n, m = map(int, input().split(" "))
S = []
P = []
for i in range(n): 
  S.append(input())
for i in range(n):
  P.append(input())

I = [_ for _ in range(m)]
cnt = 0
for pair in itertools.combinations(I,3): 
  SG = set()
  PG = set()
  for cow in S: 
    SG.add((cow[pair[0]],cow[pair[1]],cow[pair[2]]))
  for cow in P: 
    PG.add((cow[pair[0]],cow[pair[1]],cow[pair[2]]))
  if len(SG.intersection(PG)) == 0: 
    cnt += 1

print(cnt)