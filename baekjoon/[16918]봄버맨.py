r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]

if n == 1:
    arr = arr
elif n % 2 == 0:
    arr = [['O'] * c for _ in range(r)]
else:
    for _ in range(n // 2):
        visited = [[False] * c for _ in range(r)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O':
                    visited[i][j] = True
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < r and 0 <= ny < c:
                            visited[nx][ny] = True

        for i in range(r):
            for j in range(c):
                if visited[i][j] == False:
                    arr[i][j] = 'O'
                else:
                    arr[i][j] = '.'

for row in arr:
    print(''.join(row))

