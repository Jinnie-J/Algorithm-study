#조합구하기 응용
def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for i in range(len(hs)):
            x1 = hs[i][0]
            y1 = hs[i][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x2 - x1) + abs(y2 - y1))
            sum += dis
        if sum < res:
            res = sum

        else:
            for i in range(s, len(pz)):
                cb[L] = i
                DFS(L + 1, i + 1)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
hs = []
pz = []
cb = [0] * m
res = 2147000000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            hs.append((i, j))
        if board[i][j] == 2:
            pz.append((i, j))
DFS(0, 0)

print(res)
