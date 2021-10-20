import queue


def solution(number, target):
    answer = 0
    visited = [0 for _ in range(10001)]
    q = queue.Queue()
    q.put(number)
    visited[number] = 1
    while not q.empty():
        x = q.get()
        if x == target:
            break
        if x + 1 <= 10000 and visited[x + 1] == 0:
            visited[x + 1] = visited[x] + 1
            q.put(x + 1)
        if x - 1 >= 0 and visited[x - 1] == 0:
            visited[x - 1] = visited[x] + 1
            q.put(x - 1)
        if x * 2 <= 10000 and visited[x * 2] == 0:
            visited[x * 2] == visited[x] + 1
            q.put(x * 2)
    answer = visited[target] - 1
    return answer


# 테스트케이스 출력 코드
number1 = 5
target1 = 9
ret1 = solution(number1, target1)
print("solution 함수의 반환 값은", ret1, "입니다.")
