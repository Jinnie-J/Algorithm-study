def solution(l, v):
    answer = 0
    v.sort()

    arr = []

    if 0 < v[0]:
        arr.append(v[0])

    for x, y in zip(v[1:], v[:-1]):
        if (x - y) % 2 == 0:
            distance = (x - y) // 2
        else:
            distance = (x - y) // 2 + 1
        arr.append(distance)

    if l > v[-1]:
        arr.append(l - v[-1])

    return max(arr)

    return answer
