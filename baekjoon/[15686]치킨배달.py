n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def dfs(L, s):
    global res
    if L == m:
        sumdis = 0
        for i in range(len(hs)):
            mindis = 2147000000
            for x in arr:
                mindis = min(mindis, abs(hs[i][0] - ch[x][0]) + abs(hs[i][1] - ch[x][1]))
            sumdis += mindis
        if res > sumdis:
            res = sumdis
    else:
        for i in range(s, len(ch)):
            arr[L] = i
            dfs(L + 1, i + 1)


hs = []
ch = []
arr = [0] * m
res = 2147000000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            hs.append([i, j])
        if board[i][j] == 2:
            ch.append([i, j])
dfs(0, 0)

print(res)
