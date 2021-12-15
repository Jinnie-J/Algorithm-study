n = int(input())
arr = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

maxarr = -2147000000
minarr = 2147000000


def dfs(num, idx, add, minus, mul, div):
    global minarr, maxarr
    if idx == n:
        maxarr = max(maxarr, num)
        minarr = min(minarr, num)
        return
    if add > 0:
        dfs(num + arr[idx], idx + 1, add - 1, minus, mul, div)
    if minus > 0:
        dfs(num - arr[idx], idx + 1, add, minus - 1, mul, div)
    if mul > 0:
        dfs(num * arr[idx], idx + 1, add, minus, mul - 1, div)
    if div > 0:
        dfs(int(num / arr[idx]), idx + 1, add, minus, mul, div - 1)


dfs(arr[0], 1, a, b, c, d)

print(maxarr)
print(minarr)
