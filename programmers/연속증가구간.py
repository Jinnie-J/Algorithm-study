def solution(arr):
    dp = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            dp[i] = dp[i - 1] + 1
    answer = max(dp)
    return answer


arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
