n = int(input())
notes = list(int(input()) for i in range(n))
c = int(input())
chord = list(int(input()) for i in range(c))

def check(s): 
  cur = notes[s:s+c]
  dif = sorted(cur)[0]-sorted(chord)[0]
  for i in range(c): 
    if sorted(cur)[i]-sorted(chord)[i] != dif: 
      return False
  return True

k = 0
K = []
for i in range(n-c+1): 
  if check(i): 
    k += 1
    K.append(i+1)

print(k)
for item in K: 
  print(item)