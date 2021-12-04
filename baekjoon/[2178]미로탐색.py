from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue.append([0, 0])

while queue:
    tmp = queue.popleft()
    a = tmp[0]
    b = tmp[1]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
            queue.append([x, y])
            arr[x][y] = arr[a][b] + 1
print(arr[n - 1][m - 1])
