def dfs(start, computers, visited):
    visited[start] = 1
    for i in range(len(computers)):
        if visited[i] == 0 and computers[start][i] == 1:
            visited[i] = 1
            dfs(i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(len(computers)):
        if visited[i] == 0:
            answer += 1
            dfs(i, computers, visited)
    return answer
