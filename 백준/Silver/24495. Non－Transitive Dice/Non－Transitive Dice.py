t = int(input())

def beat(a,b):
    count = [0,0]
    for i in a:
        for j in b:
            count[0] += 1 if i>j else 0
            count[1] += 1 if i<j else 0
    if count[0] > count[1]:
        return 0
    elif count[1] > count[0]: 
        return 1
    else:
        return -1

ans = []
for i in range(t):
    li = list(map(int, input().split(" ")))
    a, b = li[0:4], li[4:8]
    tmp = "no"
    check = False
    
    for i in range(1,11): 
        for j in range(1,11): 
            for k in range(1,11): 
                for l in range(1,11):  
                    c = [i,j,k,l] 
                    if beat(a,b) == beat(b,c) == beat(c,a) != -1: 
                        tmp = "yes"
                        check = True
                        break
                if check == True : break
            if check == True : break
        if check == True : break
    
    ans.append(tmp)

for an in ans:
    print(an)