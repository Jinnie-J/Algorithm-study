#소용돌이 수의 대각선 합 구하기
def solution(n):
    answer = 0
    arr = []
    j = 1

    for i in range(n):
        arr.append([])
        for _ in range(n):
            arr[i].append(j)
            j += 1

    for k in range(n):
        if k % 2 == 0:
            answer += arr[k][k]
        else:
            answer += arr[k][n - k - 1]
    return answer
