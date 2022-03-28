from collections import deque

def solution(n, m, image):
    answer = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if image[i][j] == 0:
                continue

            color = image[i][j]
            q = deque([(i, j)])
            image[i][j] = 0

            while q:
                x, y = q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == color:
                        image[nx][ny] = 0
                        q.append((nx, ny))
            answer += 1

    return answer
