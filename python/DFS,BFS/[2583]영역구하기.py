# DFS 문제풀이
import sys

sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
answer = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    arr[x][y] = 1
    for i in range(4):
        nx = x + dy[i]
        ny = y + dx[i]
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
            dfs(nx, ny)

for i in range(k):
    b1, a1, b2, a2 = map(int, input().split())
    a1 = m - a1
    a2 = m - a2
    for j in range(min(a1, a2), max(a1, a2)):
        for k in range(min(b1, b2), max(b1, b2)):
            arr[j][k] -= 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i], end=' ')
