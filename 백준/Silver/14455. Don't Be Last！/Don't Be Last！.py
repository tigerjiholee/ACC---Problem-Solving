n = int(input())
log = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0, "Maggie":0, "Henrietta":0}
for i in range(n):
  name, num = input().strip().split(" ")
  log[name] += int(num)

if len(set(log.values())) == 1:
  print("Tie")
else:
  m = sorted(list(set(log.values())))[1]
  ans = ""
  for cow in log.keys():
    if log[cow] == m:
      ans = cow if ans == "" else "Tie"
  print(ans)