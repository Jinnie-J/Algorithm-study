from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for x in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), x)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            for c in counter:
                if counter[c] == max(counter.values()):
                    answer.append(''.join(c))
    answer.sort()
    return answer
