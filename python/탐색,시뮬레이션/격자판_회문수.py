board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        if board[j][i] == board[j + 4][i] and board[j + 1][i] == board[j + 3][i]:
            cnt += 1
        if board[i][j] == board[i][j + 4] and board[i][j + 1] == board[i][j + 3]:
            cnt += 1

print(cnt)
