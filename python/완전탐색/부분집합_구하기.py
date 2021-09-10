# 상태트리 구현.  1~n까지 숫자를 사용 할 때와 아닐 때를 나눠서 dfs 함수 호출
def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        dfs(v + 1)
        ch[v] = 0
        dfs(v + 1)


n = int(input())
ch = [0] * (n + 1)
dfs(1)
