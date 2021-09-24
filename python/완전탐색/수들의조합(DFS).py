def dfs(L, s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            for x in res:
                print(x, end=' ')
            print()
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = arr[i]
            dfs(L + 1, i + 1)


n, k = map(int, input().split())
res = [0] * k
cnt = 0
arr = list(map(int, input().split()))
m = int(input())

dfs(0, 0)
print(cnt)
