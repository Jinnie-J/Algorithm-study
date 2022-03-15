import math


def solution(monster, S1, S2, S3):
    answer = -1

    all = S1 * S2 * S3
    mons = all

    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                if (i + j + k + 1) in monster:
                    mons -= 1

    answer = (mons / all) * 1000
    answer = math.trunc(answer)

    return answer
