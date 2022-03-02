def solution(board, nums):
    answer = 0
    nums = set(nums)
    visited = [[False] * len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in nums:
                visited[i][j] = True
    # 가로 빙고 체크
    for x in visited:
        for y in x:
            if y == False:
                break
        else:
            answer += 1

    # 세로 빙고 체크
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[j][i] == False:
                break
        else:
            answer += 1

    # 왼쪽 대각선 빙고 체크
    for i in range(len(visited)):
        if visited[i][i] == False:
            break
    else:
        answer += 1

    # 오른쪽 대각선 빙고 체크
    for i in range(len(visited)):
        if visited[i][len(visited) - 1 - i] == False:
            break
    else:
        answer += 1

    return answer


# 간단한 풀이
def solution(board, nums):
    answer = 0
    nums = set(nums)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in nums:
                board[i][j] = 0
    # 가로
    answer += len([i for i in board if sum(i) == 0])
    # 세로
    answer += len([i for i in zip(*board) if sum(i) == 0])
    # 대각선
    answer += int(sum(board[i][i] for i in range(len(board))) == 0)
    answer += int(sum(board[len(board) - 1 - i][i] for i in range(len(board))) == 0)

    return answer
