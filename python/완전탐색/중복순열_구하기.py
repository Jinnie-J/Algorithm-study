def dfs(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            res[L] = i
            dfs(L + 1)


n, m = map(int, input().split())
res = [0] * m
cnt = 0
dfs(0)
print(cnt)
