def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = citations[0]
    for i in range(n, -1, -1):
        index = 0
        while index < len(citations) and citations[index] >= i:
            index += 1
        if index >= i:
            answer = i
            break
    return answer
