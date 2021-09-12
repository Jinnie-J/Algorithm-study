import sys


def dfs(L, sum):
    if L == len(arr):
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        dfs(L + 1, sum + arr[L])
        dfs(L + 1, sum)


n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
dfs(0, 0)
print("NO")
