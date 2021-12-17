import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direction = [[],
             [[0], [1], [2], [3]],
             [[0, 1], [2, 3]],
             [[0, 2], [1, 2], [1, 3], [0, 3]],
             [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
             [[0, 1, 2, 3]]
             ]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

cctv = []
cctvcnt = 0

# cctv count
for i in range(m):
    for j in range(n):
        if 0 < arr[i][j] < 6:
            cctv.append((i, j, arr[i][j]))
            cctvcnt += 1


# 사각지대 count
def zerocount(arr):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1
    return cnt


minarea = 2147000000


def dfs(arr, idx):
    global minarea
    tmp = copy.deepcopy(arr)
    if idx == cctvcnt:
        minarea = min(minarea, zerocount(tmp))
        return
    x, y, cctvnum = cctv[idx]
    for d in direction[cctvnum]:
        move(x, y, d, tmp)
        dfs(tmp, idx + 1)
        tmp = copy.deepcopy(arr)


def move(x, y, d, arr):
    for dir in d:
        nx, ny = x, y
        while True:
            nx += dx[dir]
            ny += dy[dir]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] != 6:
                arr[nx][ny] = '#'
            else:
                break


dfs(arr, 0)
print(minarea)
