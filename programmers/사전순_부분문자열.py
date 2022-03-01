# 조합 사용하여 시간초과 발생한 풀이
from itertools import combinations

def solution(s):
    answer = ''
    arr = []

    for i in range(1, len(s)):
        for x in list(map(''.join, combinations(s, i))):
            arr.append(x)

    arr.sort()
    return arr[-1]


# 스택 사용하여 성공한 풀이
def solution(s):
    stack = []

    for x in s:
        while stack and stack[-1] < x:
            stack.pop()
        stack.append(x)

    return ''.join(stack)
