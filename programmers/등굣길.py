def solution(m, n, puddles):
    arr = [[0] * (m + 1) for _ in range(n + 1)]
    arr[1][1] = 1

    for x, y in puddles:
        arr[y][x] = -1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if arr[x][y] == -1:
                arr[x][y] = 0
                continue

            arr[x][y] += (arr[x - 1][y] + arr[x][y - 1]) % 1000000007

    return arr[n][m]
