n = int(input())
var = {"B":[0,0], "E":[0,0], "S":[0,0], "I":[0,0], "G":[0,0], "O":[0,0], "M":[0,0]}
for i in range(n):
  a, b = input().split(" ")
  var[a][int(b)%2] += 1

ans = 0
for b in range(2):
  for e in range(2):
    for s in range(2):
      for i in range(2):
        for g in range(2):
          for o in range(2):
            for m in range(2):
              if (b+e+s+s+i+e)*(g+o+e+s)*(m+o+o) % 2 == 0:
                ans += var["B"][b]*var["E"][e]*var["S"][s]*var["I"][i]*var["G"][g]*var["O"][o]*var["M"][m]

print(ans)