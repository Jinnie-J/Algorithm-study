dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and board[xx][yy] == 1:
            dfs(xx, yy)


n = int(input())
board = [list(map(int, input())) for _ in range(n)]

cnt = 0
arr = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            arr.append(cnt)

print(len(arr))
arr.sort()
for i in range(len(arr)):
    print(arr[i])
