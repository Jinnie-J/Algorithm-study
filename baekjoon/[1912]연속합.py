# 시간복잡도 O(N^2)로 시간초과 발생한 코드
n = int(input())
arr = list(map(int, input().split()))
sumArr = []
for i in range(len(arr)):
    answer = arr[i]
    result = arr[i]
    for j in range(i + 1, len(arr)):
        answer += arr[j]
        result = max(answer, result)
    sumArr.append(result)
print(max(sumArr))

# DP 사용하여 해결
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
print(max(dp))
