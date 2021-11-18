# 분할정복 문제
def quadtree(x, y, n):
    global result
    check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != check:
                result += "("
                quadtree(x, y, n // 2)
                quadtree(x, y + n // 2, n // 2)
                quadtree(x + n // 2, y, n // 2)
                quadtree(x + n // 2, y + n // 2, n // 2)
                result += ")"
                return
    result += str(check)


n = int(input())
arr = [list(input()) for _ in range(n)]

result = ""
quadtree(0, 0, n)
print(result)
