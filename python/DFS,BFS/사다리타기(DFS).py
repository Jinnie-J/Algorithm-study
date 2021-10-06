#사다리타기 문제 - 맨 아래에서부터 올라가며 시작 위치 확인
def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if 0 <= y + 1 <= 9 and board[x][y + 1] == 1 and ch[x][y + 1] == 0:
            dfs(x, y + 1)
        elif 0 <= y - 1 <= 9 and board[x][y - 1] == 1 and ch[x][y - 1] == 0:
            dfs(x, y - 1)
        else:
            dfs(x - 1, y)


ch = [[0] * 10 for _ in range(10)]
board = [list(map(int, input().split())) for _ in range(10)]

for i in range(10):
    if board[9][i] == 2:
        des = i
        break
dfs(9, des)
