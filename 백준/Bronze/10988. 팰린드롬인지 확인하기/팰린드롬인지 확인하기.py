import sys; input = sys.stdin.readline
string = input().strip()
a = 1
for i in range(0,len(string)//2+1):
  if string[i] != string[len(string)-1-i]:
    a = 0
    break
print(a)