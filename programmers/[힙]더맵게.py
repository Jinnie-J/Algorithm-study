import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        a = heapq.heappop(scoville)
        if a < K:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + (b * 2))
            answer += 1
        else:
            return answer
