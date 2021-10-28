
# 런타임에러 해결 - k가 0일때 break, k보다 큰 수 일때 continue
n, k = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

answer = 0

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if arr[i] > k:
        continue

    answer += k // arr[i]
    k = k % arr[i]

print(answer)
