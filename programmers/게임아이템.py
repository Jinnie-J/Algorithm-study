# 효율성 시간초과 발생한 풀이
def solution(healths, items):
    answer = []

    healths.sort()
    checked = [False] * len(items)

    for i in range(len(healths)):
        maxValue = 0
        maxIndex = -1
        for j in range(len(items)):
            if healths[i] - items[j][1] >= 100 and not checked[j]:
                if items[j][0] > maxValue:
                    maxValue = items[j][0]
                    maxIndex = j

        if maxIndex != -1:
            checked[maxIndex] = True
            answer.append(maxIndex + 1)

    answer.sort()

    return answer


#heapq 사용한 풀이
from heapq import heappush, heappop
from collections import deque

def solution(healths, items):
    healths.sort()
    items = deque(sorted([(item[1], item[0], index+1) for index, item in enumerate(items)])) # 깎는 체력 순으로 정렬
    answer = []
    heap = []

    for health in healths:
        while items:
            debuff, buff, index = items[0] # 가장 깎는 체력이 낮은 아이템
            if health - debuff < 100:
                break
            items.popleft()
            heappush(heap, (-buff, index))

        if heap:
            buff, index = heappop(heap)
            answer.append(index)

    return sorted(answer)