n = int(input())
li = []
for i in range(n): 
  a, b = input().strip().split(" ")
  a_chr, b_chr = [0]*26, [0]*26
  for c in a:
    a_chr[ord(c)-97] += 1
  for c in b:
    b_chr[ord(c)-97] += 1
  tmp = []
  for i in range(26):
    if max(a_chr[i], b_chr[i]) > 0:
      for j in range(max(a_chr[i], b_chr[i])): 
        tmp.append(chr(i+97))
  li.append(tmp)

ans = [0] * 26
for row in li:
  for let in row: 
    ans[ord(let)-97] += 1

for a in ans:
  print(a)