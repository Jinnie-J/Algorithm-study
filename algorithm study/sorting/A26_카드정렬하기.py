#우선순위 큐 이용
import heapq

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum = (first + second)
    result += sum
    heapq.heappush(heap, sum)

print(result)
