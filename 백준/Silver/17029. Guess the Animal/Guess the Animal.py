import sys; input = sys.stdin.readline
import itertools

n = int(input())
C = {}
for i in range(n):
  tmp = list(input().strip().split(" "))
  C[tmp[0]] = tmp[2:]

ans = []
for pair in itertools.combinations(C.keys(), 2):
  ans.append(len(set(C[pair[0]]).intersection(set(C[pair[1]]))))
  #print(set(C[pair[0]]), set(C[pair[1]]), ans[-1])
print(max(ans)+1)