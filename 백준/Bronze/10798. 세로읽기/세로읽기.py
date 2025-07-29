import sys; input = sys.stdin.readline

words = []
for i in range(5):
    words.append(list(input().strip()))

string = ""
for i in range(max(len(x) for x in words)): 
    for j in range(5):
        try:
            string += words[j][i]
        except:
            pass

print(string)