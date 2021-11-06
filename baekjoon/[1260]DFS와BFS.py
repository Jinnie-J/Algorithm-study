from collections import deque

#너비우선탐색(큐 사용)
def bfs(v):
    q = deque()
    q.append(v)
    visited_list[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_list[i] = 1

#깊이우선탐색(재귀함수 사용)
def dfs(v):
    visited_list2[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited_list = [0] * (n + 1)
visited_list2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
