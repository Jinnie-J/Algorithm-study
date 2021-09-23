def dfs(L, sum):
    global res
    if L == k:
        if 0 < sum <= s:
            res.add(sum)
    else:
        dfs(L + 1, sum + arr[L])
        dfs(L + 1, sum - arr[L])
        dfs(L + 1, sum)


k = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
res = set()
dfs(0, 0)

print(s - len(res))
