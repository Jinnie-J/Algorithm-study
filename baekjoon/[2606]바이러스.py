arr = []
answer = []
n = int(input())
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

ch = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(m):
    ch[arr[i][0] - 1][arr[i][1] - 1] = 1
    ch[arr[i][1] - 1][arr[i][0] - 1] = 1

def virus(x, y):
    answer.append(y)
    for i in range(n):
        if ch[y][i] == 1 and visited[y][i] == 0:
            visited[y][i] = 1
            virus(y, i)

for i in range(n):
    if ch[0][i] == 1 and visited[0][i] == 0:
        visited[0][i] = 1
        virus(0, i)

answer = set(answer)
print(len(answer) - 1)
