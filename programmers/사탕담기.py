from itertools import combinations

def solution(m, weights):
    answer = 0
    arr = []

    for i in range(1, len(weights)):
        arr += ([sum(c) for c in combinations(weights, i)])

    for x in arr:
        if x == m:
            answer += 1

    return answer
