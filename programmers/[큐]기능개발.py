import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    arr = []

    for i in range(len(progresses)):
        arr.append(math.ceil((100 - progresses[i]) / speeds[i]))

    q = deque(arr)

    while q:
        day = q.popleft()
        count = 1
        while q and q[0] <= day:
            count += 1
            q.popleft()

        answer.append(count)

    return answer
