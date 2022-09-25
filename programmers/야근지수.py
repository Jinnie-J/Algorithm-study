
#효율성 테스트 시간초과 코드
def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    while n > 0:
        for i in range(len(works)):
            if works[i] == max(works):
                works[i]-=1
                n-=1
                break
                
    answer = sum([i*i for i in works])
    
    return answer

#최대 힙 이용하여 해결
import heapq
def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    heap=[]
    for work in works:
        heapq.heappush(heap, -work)
    
    while n > 0:
        heapq.heappush(heap, heapq.heappop(heap)+1)
        n-=1
        
    for i in range(len(heap)):
        answer += (heap[i]*heap[i])
        
    return answer