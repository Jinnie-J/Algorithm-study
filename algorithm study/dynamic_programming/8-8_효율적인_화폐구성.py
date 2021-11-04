
#냅색 알고리즘 활용
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

answer = [1000] * (m + 1)
answer[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        answer[j] = min(answer[j], answer[j - arr[i]] + 1)

if answer[m] != 1000:
    print(-1)
else:
    print(answer[m])
