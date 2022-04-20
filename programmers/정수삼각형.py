# dfs로 풀이하여 시간초과 발생
def dfs(arr, x_index, y_index, result, answer):
    if x_index == len(arr):
        answer.append(result)

    else:
        dfs(arr, x_index + 1, y_index, result + arr[x_index][y_index], answer)
        dfs(arr, x_index + 1, y_index + 1, result + arr[x_index][y_index + 1], answer)


def solution(triangle):
    answer = []
    dfs(triangle, 1, 0, triangle[0][0], answer)
    return max(answer)


# dp 사용하여 해결
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    return max(triangle[-1])
