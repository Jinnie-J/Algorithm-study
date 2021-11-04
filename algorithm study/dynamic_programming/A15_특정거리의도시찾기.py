n, m, k, x = map(int, input().split())
dis = [[10001] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dis[i][i] = 0
for i in range(m):
    a, b = map(int, input().split())
    dis[a][b] = 1

for p in range(1, n + 1):
    for j in range(1, n + 1):
        dis[x][j] = min(dis[x][j], dis[x][p] + dis[p][j])

check = False
for i in range(1, n + 1):
    if dis[x][i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

# BFS(큐) 사용으로 메모리 초과 해결한 코드
import sys

input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
