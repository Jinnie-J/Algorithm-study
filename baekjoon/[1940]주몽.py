# 모든 경우를 탐색하여 시간초과 발생한 코드
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(n - 1):
    for j in range(i, n):
        if arr[i] + arr[j] == m:
            cnt += 1

print(cnt)

# 투 포인터 풀이 코드
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

i, j = 0, n - 1

while i < j:
    if arr[i] + arr[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] < m:
        i += 1
    else:
        j -= 1

print(cnt)
