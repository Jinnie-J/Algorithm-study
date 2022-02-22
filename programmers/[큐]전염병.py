from collections import deque


def solution(m, n, infests, vaccinateds):
    answer = 0
    cnt = len(infests)

    arr = [[0] * n for _ in range(m)]

    for x in infests:
        arr[x[0] - 1][x[1] - 1] = 1

    for x in vaccinateds:
        arr[x[0] - 1][x[1] - 1] = -1

    q = deque()
    for x in infests:
        q.append([x[0] - 1, x[1] - 1, 0])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        # L을 통해서 깊이(몇 번 반복하였는지) 체크
        x, y, L = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                cnt += 1
                arr[nx][ny] = 1
                q.append([nx, ny, L + 1])

    if (cnt + len(vaccinateds)) != m * n:
        answer = -1
        return answer

    answer = L

    return answer
