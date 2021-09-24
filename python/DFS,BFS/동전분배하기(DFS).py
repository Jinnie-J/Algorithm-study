def dfs(L, a, b, c):
    global res
    if L == n:
        if a != b and b != c and a != c:
            ans = max(a, b, c) - min(a, b, c)
            if ans < res:
                res = ans
    else:
        dfs(L + 1, a + arr[L], b, c)
        dfs(L + 1, a, b + arr[L], c)
        dfs(L + 1, a, b, c + arr[L])


n = int(input())
arr = []

res = 2147000000
for _ in range(n):
    arr.append(int(input()))

dfs(0, 0, 0, 0)
print(res)
