import copy
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and tmparr[nx][ny] == 1:
            dfs(nx, ny)


maxarr = 0
for i in range(n):
    maxarr = max(maxarr, max(arr[i]))

maxcnt = 0
for i in range(maxarr + 1):
    tmparr = copy.deepcopy(arr)
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if tmparr[j][k] <= i:
                tmparr[j][k] = 0
            else:
                tmparr[j][k] = 1

    for j in range(n):
        for k in range(n):
            if tmparr[j][k] == 1 and visited[j][k] == 0:
                dfs(j, k)
                cnt += 1
    maxcnt = max(maxcnt, cnt)
print(maxcnt)
