from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, usado = (map(int, input().split()))
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for i in range(q):
    k, v = map(int, input().split())
    visited = [False] * (n + 1)
    visited[v] = True
    q = deque([(v, float('inf'))])
    answer = 0

    while q:
        v, usado = q.pop()
        for v2, usado2 in graph[v]:
            usado2 = min(usado, usado2)
            if usado2 >= k and not visited[v2]:
                answer += 1
                q.append((v2, usado2))
                visited[v2] = True
    print(answer)