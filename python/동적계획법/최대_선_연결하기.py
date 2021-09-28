
n= int(input())
arr = list(map(int, input().split()))
dy = [0] * n
dy[0] = 1
for i in range(1, n):
    res = 0
    for j in range(i):
        if arr[j] < arr[i]:
            if dy[j] > res:
                res = dy[j]
    dy[i] = res + 1
print(max(dy))
