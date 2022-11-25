from collections import deque


# BFS 풀이
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


# DFS 풀이 - 재귀 호출 횟수 설정 필요
from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)


def solution(n, m, images):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    count = 0

    def dfs(arr, x, y, num):
        if arr[x][y] == 0:
            return
        arr[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 0 and arr[nx][ny] == num:
                    dfs(arr, nx, ny, num)

    for i in range(n):
        for j in range(m):
            if images[i][j] != 0:
                dfs(images, i, j, images[i][j])
                count += 1
    return count
