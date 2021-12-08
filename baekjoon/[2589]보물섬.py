#최단거리(bfs) 현재 위치까지의 거리 = 이전 위치까지의 거리 값 + 1
from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

def bfs(x, y):
    dis = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    q.append((x, y))
    maxdis = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                maxdis = max(maxdis, visited[nx][ny])
    return maxdis - 1


answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)
