from collections import deque


def solution(n, edge):
    answer = 0
    arr = [[] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for x, y in edge:
        arr[x].append(y)
        arr[y].append(x)
    visited[1] = 1
    q = deque([1])
    while q:
        n = q.popleft()
        for x in arr[n]:
            if visited[x] == 0:
                q.append(x)
                visited[x] = visited[n] + 1

    answer = visited.count(max(visited))

    return answer
