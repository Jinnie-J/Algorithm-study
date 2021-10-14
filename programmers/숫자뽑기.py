# dfs- 조합구하기를 활용한 풀이
def dfs(L, s):
    global answer
    if L == k:
        if max(res) - min(res) < answer:
            answer = max(res) - min(res)
    else:
        for i in range(s, len(arr)):
            res[L] = arr[s]
            dfs(L + 1, s + 1)


arr = [9, 11, 9, 6, 4, 19]
k = 4
res = [0] * k
answer = 214700000
dfs(0, 0)
print(answer)


# 배열을 정렬한 다음, 배열의 (1~k번째) ~ (n-k+1~n번째)씩 나누어 가장 큰 값과 작은 값의 차를 구하여 그 중 최솟값을 구하면 된다.
def solution(arr, k):
    answer = 214700000
    arr.sort()
    for i in range(len(arr) - k + 1):
        answer = min(arr[i + k - 1] - arr[i])
    return answer


arr = [9, 11, 9, 6, 4, 19]
k = 4
ret = solution(arr, k)
print(ret)
