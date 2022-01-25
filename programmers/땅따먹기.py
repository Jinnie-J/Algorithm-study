# dfs 사용. 런타임에러 발생한 코드
def solution(land):
    answer = 0

    def dfs(L, sum, row):
        nonlocal answer
        if L == len(land):
            answer = max(answer, sum)
        else:
            for i in range(4):
                if i != row:
                    dfs(L + 1, sum + land[L][i], i)

    for i in range(4):
        dfs(0, 0, i)

    return answer

# 메모이제이션 활용 코드
def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i - 1][:j] + land[i - 1][j + 1:]) + land[i][j]
    return max(land[-1])
