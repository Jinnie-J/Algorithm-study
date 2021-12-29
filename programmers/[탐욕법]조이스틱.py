def updown(alpha):
    if ord(alpha) > 78:
        return 90 - ord(alpha) + 1
    else:
        return ord(alpha) - 65


def solution(name):
    answer = 0
    next = 0
    result = len(name) - 1

    for i in range(len(name)):
        if name[i] != 'A':
            answer += updown(name[i])

            next = i + 1
            while next < len(name) and name[next] == 'A':
                next += 1

            result = min(result, i + i + len(name) - next)

    answer += result

    return answer
