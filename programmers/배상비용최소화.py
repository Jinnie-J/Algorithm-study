# sort 이용한 풀이
def solution(n, works):
    result = 0

    if n >= sum(works):
        return 0;

    for _ in range(n):
        works.sort()
        works[-1] -= 1

    for x in works:
        result += x * x
    return result


# heapq 이용한 풀이
import heapq


def solution(n, works):
    result = 0

    if n >= sum(works):
        return 0;

    works = [-i for i in works]  # max heap
    heapq.heapify(works)

    for _ in range(n):
        work = heapq.heappop(works) + 1
        heapq.heappush(works, work)

    return sum([i ** 2 for i in works])
