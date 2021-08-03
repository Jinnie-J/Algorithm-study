from collections import deque

# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
# (1,1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
# 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
