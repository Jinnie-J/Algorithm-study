def solution(N, stages):
    answer = []
    d = {}
    stages.sort()
    for i in range(1, N + 1):
        fail_cnt = 0
        clear_cnt = 0
        for x in stages:
            if x >= i:
                if x == i:
                    fail_cnt += 1
                clear_cnt += 1
        if clear_cnt != 0 and fail_cnt != 0:
            answer.append(fail_cnt / clear_cnt)
        else:
            answer.append(0)

    for i in range(1, len(answer) + 1):
        d[i] = answer[i - 1]

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)

    result = []
    for x in d:
        result.append(x[0])

    return result

# 간결한 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)