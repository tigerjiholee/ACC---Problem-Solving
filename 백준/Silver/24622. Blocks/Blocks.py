import sys; input = sys.stdin.readline
import itertools

n = int(input())
D = []
for i in range(4):
    D.append(input().strip())
T = []
for i in range(n): 
    T.append(input().strip())

for word in T: 
    ans = "NO"
    for comb in itertools.permutations(D, len(word)): 
        check = 0
        for i in range(len(word)): 
            if word[i] not in comb[i]: 
                break
            else: 
                check += 1
        if check == len(word): 
            ans = "YES"
            break
    print(ans)