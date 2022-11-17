n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(arr, x, y):
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                dfs(arr, nx, ny)


cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
            dfs(arr, i, j)

print(cnt)

# 책 풀이
# 맨 왼쪽부터 차례로 탐색해 0인 위치를 찾아 그 지점을 기준으로 연결된 모든 0인 부분을 1로 바꿔주면 결과적으로 연결된 부분을 한 번만 카운트하게 된다.
n, m = map(int, input().split())
count = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# 1. 시작 점 부터 칸의 값이 0이면, 해당 칸 1로 바꿔주기
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 2. 상,하,좌,우 칸 모두 1로 바꿔주기
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


# 3. 첫번째 칸부터 마지막 조회하여 칸 까지 값이 0일 경우에만 count 해주기
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)
