def solution(priorities, location):
    answer = 0
    from collections import deque

    queue = deque([(v, i) for i, v in enumerate(priorities)])

    while len(queue):
        now = queue.popleft()
        # 배열의 마지막 원소일 경우도 처리
        if queue and now[0] < max(queue)[0]:
            queue.append(now)
        else:
            answer += 1
            if now[1] == location:
                break

    return answer
