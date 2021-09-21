
#Cut Edge Tech  L(count)이 현재의 최솟값(res)을 넘어버리면 return
def dfs(L, sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        if sum < m:
            for i in range(n):
                dfs(L + 1, sum + arr[i])


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr.sort(reverse=True)
res = 2147000000

dfs(0, 0)
print(res)
