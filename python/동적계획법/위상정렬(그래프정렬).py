# 해당 좌표보다 먼저 해야하는 일이 몇개인지를 담은 degree 배열 이용 - degree가 0이 되었을 때 출력
from collections import deque

n, m = map(int, input().split())
arr = []
degree = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])
    degree[b - 1] += 1

ch = [0] * n
Q = deque()
for i in range(n):
    if degree[i] == 0:
        ch[i] = 1
        Q.append(i)
answer = []
while Q:
    tmp = Q.popleft()
    answer.append(tmp)
    for i in range(m):
        if arr[i][0] == tmp + 1:
            degree[arr[i][1] - 1] -= 1
    for i in range(n):
        if degree[i] == 0 and ch[i] == 0:
            ch[i] = 1
            Q.append(i)

for i in range(m):
    print(answer[i] + 1, end=' ')

# 그래프 활용 풀이법
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
dQ = deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1
for i in range(1, n + 1):
    if degree[i] == 0:
        dQ.append(i)
while dQ:
    x = dQ.popleft()
    print(x, end=' ')
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dQ.append(i)
