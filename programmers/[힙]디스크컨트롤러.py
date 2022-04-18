def solution(jobs):
    n = len(jobs)
    answer = 0
    # 소요시간을 기준으로 정렬
    jobs = sorted(jobs, key=lambda x: x[1])
    start = 0

    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                #소요시간을 기준으로 정렬하였으니, 가장 첫번째 값만 pop
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                start += 1
    return answer // n


# 힙 사용한 풀이
import heapq

def solution(jobs):
    answer = 0
    start, now = -1, 0
    heap = []

    i = 0
    while i < len(jobs):
        for j in jobs:
            #현재 구간에 해당하는 항목들 힙에 담기
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        #힙에 담긴 항목 중 소요시간이 가장 짧은 것 heappop
        if len(heap) > 0:
            tmp = heapq.heappop(heap)
            start = now
            now += tmp[0]
            answer += now - tmp[1]
            i += 1
        else:
            now += 1

    return answer // len(jobs)
