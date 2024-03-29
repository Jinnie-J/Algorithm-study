def check(arr):
    for i in range(9):
        ch1 = [0] * 9
        ch2 = [0] * 9
        for j in range(9):
            ch1[board[i][j] - 1] = 1
            ch2[board[j][i] - 1] = 1

        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 9
            for k in range(3):
                for s in range(3):
                    ch3[board[i * 3 + k][j * 3 + s] - 1] = 1

            if sum(ch3) != 9:
                return False
    return True


board = [list(map(int, input().split())) for _ in range(9)]

if (check(board)):
    print("YES")
else:
    print("NO")
