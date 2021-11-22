from collections import deque
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0


def bfs():
    global answer
    q = deque()
    copyarr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if copyarr[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and copyarr[nx][ny] == 0:
                copyarr[nx][ny] = 2
                q.append([nx, ny])
    cnt = 0
    for i in copyarr:
        cnt += i.count(0)
    answer = max(answer, cnt)


def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x + 1)
                arr[i][j] = 0

wall(0)
print(answer)
