from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for x in cities:
        tmp = x.upper()
        if tmp in q:
            q.remove(tmp)
            q.append(tmp)
            answer += 1
        else:
            if len(q) >= cacheSize:
                q.popleft()
            q.append(tmp)
            answer += 5

    return answer
