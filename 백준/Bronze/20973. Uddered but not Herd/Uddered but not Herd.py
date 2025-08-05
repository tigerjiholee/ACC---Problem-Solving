import sys; input = sys.stdin.readline

alphs = input().strip()
lets = list(input().strip())

count = 0
check = False
while check == False:
    count += 1
    for alph in alphs:
        if len(lets) == 0:
            check=True
            break
        elif alph == lets[0]:
            lets.pop(0)

print(count)