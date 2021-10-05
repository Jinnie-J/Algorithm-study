

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(i, j):
    global cnt
    if i == 6 and j == 6:
        cnt += 1
    else:
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
                board[x][y] = 1
                dfs(x, y)
                board[x][y] = 0


cnt = 0
board = []
for i in range(7):
    board.append(list(map(int, input().split())))

board[0][0] = 1
dfs(0, 0)
print(cnt)
