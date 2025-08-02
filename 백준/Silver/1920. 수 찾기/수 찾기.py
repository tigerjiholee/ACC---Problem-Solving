n = int(input())
li = list(map(int, input().split(" ")))
li.sort()
m = int(input())
nums = list(map(int, input().split(" ")))

for num in nums:
  l = 0
  r = len(li)-1
  check = False
  while l <= r: 
    if num > li[(l+r)//2]: 
      l = (l+r)//2 + 1
    elif num < li[(l+r)//2]: 
      r = (l+r)//2 - 1
    else: 
      print(1)
      check = True
      break
  if check == False:
    print(0)