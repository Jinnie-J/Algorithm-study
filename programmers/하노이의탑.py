
# n-1개 판 2번 탑으로 옮기는 경우 + 1개 판 3번 탑으로 옮기는 경우 + n-1개 판 3번 탑으로 옮기는 경우
def hanoi(n, start, mid, end, answer):
    if n == 1:
        answer.append([start, end])
        return

    hanoi(n - 1, start, end, mid, answer)
    answer.append([start, end])
    hanoi(n - 1, mid, start, end, answer)


def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer
