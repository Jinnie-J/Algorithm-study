# deque 라이브러리 사용한 코드
from collections import deque


def solution(skill, skill_trees):
    answer = len(skill_trees)

    skillQ = deque()

    for i in range(len(skill_trees)):
        for j in range(len(skill)):
            skillQ.append(skill[j])

        tmp = list(skill_trees[i])
        for k in range(len(tmp)):
            if tmp[k] in skillQ:
                if tmp[k] != skillQ.popleft():
                    answer -= 1
                    break
        skillQ.clear()

    return answer


# 리스트로 구현한 큐
def solution(skill, skill_trees):
    answer = len(skill_trees)

    for i in range(len(skill_trees)):
        skillQ = list(skill)

        tmp = list(skill_trees[i])
        for j in range(len(tmp)):
            if tmp[j] in skillQ:
                if tmp[j] != skillQ.pop(0):
                    answer -= 1
                    break
    return answer
