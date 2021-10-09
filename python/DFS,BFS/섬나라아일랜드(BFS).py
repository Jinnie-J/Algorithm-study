# DFS활용 풀이
dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]

def dfs(x, y):
    global cnt
    board[x][y] = 0
    cnt += 1
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and board[xx][yy] == 1:
            dfs(xx, yy)

n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))
arr = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            arr.append(cnt)

print(len(arr))

# BFS활용 풀이
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt += 1
print(cnt)
