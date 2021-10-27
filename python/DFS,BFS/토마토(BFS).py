from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def tom(x, y):
    global cnt
    global arr
    global ch
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
            arr[xx][yy] = 1
            ch[xx][yy] = 1


while True:
    cntzero = 0
    ch = [[0] * n for _ in range(m)]
    for i in range(m):
        if 0 not in arr[i]:
            cntzero += 1
    if cntzero == m:
        break

    else:
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 1 and ch[i][j] == 0:
                    tom(i, j)
        cnt += 1

print(cnt)

# 큐 활용한 풀이

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
dis = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1
            Q.append((nx, ny))
flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
