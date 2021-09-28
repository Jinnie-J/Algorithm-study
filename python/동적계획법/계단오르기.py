# Bottom-Up 방식

n = int(input())

arr = [0] * (n + 1)
arr[1] = 1
arr[2] = 2

for i in range(3, n + 1):
    arr[n] = arr[n - 1] + arr[n - 2]

print(arr[n])


# Top-Down 방식


def dfs(stairs):
    if arr[stairs] != 0:
        return arr[stairs]
    if stairs == 1 and stairs == 2:
        return stairs
    else:
        arr[stairs] = dfs(stairs - 1) + dfs(stairs - 2)
        return arr[stairs]


n = int(input())
arr = [0] * (n + 1)

dfs(n)
print(arr[n])
