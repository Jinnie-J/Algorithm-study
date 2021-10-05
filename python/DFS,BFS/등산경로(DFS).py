dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] == 1
                dfs(xx, yy)
                ch[xx][yy] = 0


n = int(input())
board = [[0] * n for _ in range(n)]
ch = [[0] * n for _ in range(n)]
max = -2147000000
min = 2147000000
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max:
            max = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]

ch[sx][sy] = 1
cnt = 0
dfs(sx, sy)
print(cnt)
