dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            dfs(xx, yy, h)


cnt = 0
res = 0
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
for h in range(100):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and board[i][j] > h:
                cnt += 1
                dfs(i, j, h)
    res = max(res, cnt)
    if cnt == 0:
        break

print(res)
