li = sorted(list(map(int, input().split(" ")))) 
diff_ab = li[1]-li[0]
diff_bc = li[2]-li[1]

m, M = 0, max(diff_ab,diff_bc)

if diff_ab == 2 or diff_bc == 2 : m = 1
elif diff_ab > 2 or diff_bc > 2 : m = 2

print(m)
print(M-1)