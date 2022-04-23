import heapq


def solution(operations):
    heap = []
    for x in operations:
        oper, num = x.split()
        num = int(num)
        if oper == "D" and num == 1:
            if heap:
                max_value = max(heap)
                heap.remove(max_value)
        elif oper == "D" and num == -1:
            if heap:
                heapq.heappop(heap)
        else:
            heapq.heappush(heap, num)

    if not heap:
        return [0, 0]
    return max(heap), heap[0]
