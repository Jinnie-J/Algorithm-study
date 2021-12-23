from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    q.append([nx, ny])
                    temp.append([nx, ny])
                    visited[nx][ny] = 1
    return temp

cnt = 0
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
while True:
    visited = [[0] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    arrsum = 0
                    for x, y in temp:
                        arrsum += arr[x][y]
                    for x, y in temp:
                        arr[x][y] = arrsum // len(temp)
                    check = True
    if check == False:
        break
    cnt += 1
print(cnt)
