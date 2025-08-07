n = int(input())
log = []
for i in range(n):
  tmp = list(input().split(" "))
  log.append(tuple(sorted(tmp)))

dict = {}
for group in log:
  dict[group] = dict.get(group, 0) + 1

print(max(dict.values()))