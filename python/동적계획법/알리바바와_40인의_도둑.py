# 2차원 배열 생성할 때, 얕은 복사에 주의!
# Bottom-Up 방식
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dy = []

for i in range(n):
    dy.append([0] * n)

dy[0][0] = arr[0][0]

for i in range(1, n):
    dy[i][0] = dy[i - 1][0] + arr[i][0]
    dy[0][i] = dy[0][i - 1] + arr[0][i]

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i][j - 1] + arr[i][j], dy[i - 1][j] + arr[i][j])

print(dy[n - 1][n - 1])


# Top-Down 방식
def dfs(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = dfs(x - 1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = dfs(x, y - 1) + arr[x][y]
        else:
            dy[x][y] = min(dfs(x - 1, y), dfs(x, y - 1)) + arr[x][y]
        return dy[x][y]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)]
print(dfs(n - 1, n - 1))
