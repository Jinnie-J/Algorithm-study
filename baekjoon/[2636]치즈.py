from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()


def bfs():
    cnt = 0
    visited = [[False] * n for _ in range(m)]
    q.append((0, 0))
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 0 and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    cnt += 1
                    visited[nx][ny] = True
    return cnt


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

result = []
time = 0
while True:
    cheese = bfs()
    time += 1
    if cheese == 0:
        break
    else:
        result.append(cheese)

print(time - 1)
print(result[-1])
