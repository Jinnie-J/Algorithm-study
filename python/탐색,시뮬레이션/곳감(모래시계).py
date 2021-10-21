n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

answer = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        answer[i][j] = board[i][j]

m = int(input())
rot = []
for i in range(m):
    rot.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        if rot[i][1] == 1:
            if j - rot[i][2] < 0:
                x = n + j - rot[i][2]
                answer[rot[i][0] - 1][j] = board[rot[i][0] - 1][x]
            else:
                answer[rot[i][0] - 1][j] = board[rot[i][0] - 1][j - rot[i][2]]
        else:
            if j + rot[i][2] >= n:
                x = j + rot[i][2] - n
                answer[rot[i][0] - 1][j] = board[rot[i][0] - 1][x]
            else:
                answer[rot[i][0] - 1][j] = board[rot[i][0] - 1][j + rot[i][2]]
sumarr = 0

for i in range(n):
    if i <= n // 2:
        sumarr += sum(answer[i][i:n - i])
    else:
        sumarr += sum(answer[i][n - i - 1:i + 1])
print(sumarr)

# 배열 회전 pop 방식으로 간단하게 풀이한 코드
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h - 1].append(a[h - 1].pop(0))
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

res = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
