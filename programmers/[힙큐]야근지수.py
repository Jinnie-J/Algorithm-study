import heapq

def solution(n, works):
    answer = 0
    if n > sum(works):
        return answer

    works = [-i for i in works]
    heapq.heapify(works)

    for _ in range(n):
        work = heapq.heappop(works)
        work += 1
        heapq.heappush(works, work)

    for x in works:
        answer += x * x

    return answer
