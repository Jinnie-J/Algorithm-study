def dfs(L, sum):
    global result
    if L == n:
        if result < sum <= c:
            result = sum
    else:
        dfs(L + 1, sum + arr[L])
        dfs(L + 1, sum)


c, n = map(int, input().split())
arr = []
result = -2147000000
for _ in range(n):
    arr.append(int(input()))

dfs(0, 0)
print(result)


# Cut Edge Tech 사용하여 효율성 높인 코드
def dfs(L, sum, tsum):
    global result
    if sum + (total - tsum) < result:
        return
    if sum <= c:
        return
    if L == n:
        if result < sum:
            result = sum
    else:
        dfs(L + 1, sum + arr[L], tsum + arr[L])
        dfs(L + 1, sum, tsum + arr[L])


c, n = map(int, input().split())
arr = []
result = -2147000000
for _ in range(n):
    arr.append(int(input()))
total = sum(arr)
dfs(0, 0, 0)
print(result)
