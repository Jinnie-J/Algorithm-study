# Bottom-Up 방식
n = int(input())
a = [0] * (n + 1)

a[1] = 1
a[2] = 2

for i in range(3, n + 1):
    a[i] = a[i - 2] + a[i - 1]

print(a[n])


# Top-Down(재귀, 메모이제이션) 방식
def dfs(len):
    if a[len] > 0:
        return a[len]
    if len == 1 or len == 2:
        return len
    else:
        a[len] = dfs[len - 1] + dfs[len - 2]
        return a[len]


n = int(input())
a = [0] * (n + 1)
print(dfs[n])
