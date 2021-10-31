n, m = map(int, input().split())
arr = [0] * (n + m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i + j] += 1

maxarr = max(arr)

answer = []
for i in range(1, n + m + 1):
    if arr[i] == maxarr:
        print(i, end=' ')
