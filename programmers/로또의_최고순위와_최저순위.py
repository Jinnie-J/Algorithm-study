# 딕셔너리 사용
def solution(lottos, win_numbs):
    answer = []
    zeroCnt = 0
    correctCnt = 0
    d = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    for x in lottos:
        if x == 0:
            zeroCnt += 1
        elif x in win_numbs:
            correctCnt += 1
    maxValue = correctCnt + zeroCnt
    minValue = correctCnt

    answer.append(d[maxValue])
    answer.append(d[minValue])

    return answer


# 배열 사용
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    zeroCnt = lottos.count(0)
    answer = 0
    for x in win_nums:
        if x in lottos:
            answer += 1
    return rank[zeroCnt + answer], rank[answer]
