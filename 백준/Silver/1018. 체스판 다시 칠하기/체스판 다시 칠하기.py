import sys; input = sys.stdin.readline

n, m = map(int, input().split(" ")) 
board = []
for i in range(n):
    board.append(list(input().strip()))

ans = []
opt1 = list((list(("B", "W")*4), list(("W", "B")*4))*4)
opt2 = list((list(("W", "B")*4), list(("B", "W")*4))*4)
for i in range(0, n-7): 
    for j in range(0, m-7): 
        tmp_board = [board[x][j:j+8] for x in range(i,i+8)]
        count1, count2 = 0, 0
        for r in range(len(tmp_board)):
            for c in range(len(tmp_board[r])): 
                if tmp_board[r][c] != opt1[r][c]: 
                    count1 += 1
                if tmp_board[r][c] != opt2[r][c]: 
                    count2 += 1
        ans.append(min(count1, count2))

print(min(ans))