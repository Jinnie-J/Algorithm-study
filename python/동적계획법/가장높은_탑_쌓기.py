n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0], reverse=True)
dy = [0] * n
dy[0] = arr[0][1]
for i in range(1, n):
    res = 0
    for j in range(i):
        if arr[j][2] > arr[i][2]:
            if dy[j] > res:
                res = dy[j]
    dy[i] = res + arr[i][1]

print(max(dy))
