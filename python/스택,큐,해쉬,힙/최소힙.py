# 시간초과 난 코드
minAnswer = 21470000
arr = []
while True:
    n = int(input())
    if n == 0:
        print(minAnswer)
        arr.remove(minAnswer)
    elif n == -1:
        break
    else:
        arr.append(n)
        minAnswer = min(arr)

# heapq를 이용한 최소힙
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
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
