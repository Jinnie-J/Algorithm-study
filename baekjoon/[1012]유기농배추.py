import sys

sys.setrecursionlimit(10 ** 6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    ch[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1 and ch[nx][ny] == 0:
            dfs(nx, ny)


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    for j in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    cnt = 0
    ch = [[0] * n for _ in range(m)]
    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1 and ch[x][y] == 0:
                cnt += 1
                dfs(x, y)
    print(cnt)
