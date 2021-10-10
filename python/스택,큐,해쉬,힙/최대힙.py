# heapq를 이용한 최대힙 (부호 반대로 입력 -> 최소힙 이용)
import heapq as hq

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)
