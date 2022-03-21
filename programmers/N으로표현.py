def solution(N, number):
    answer = [set([int(str(N) * i)]) for i in range(1, 9)]

    if N == number:
        return 1

    for i in range(1, 8):
        for j in range(i):
            for y in answer[j]:
                for x in answer[i - j - 1]:
                    answer[i].add(y + x)
                    answer[i].add(y * x)
                    answer[i].add(y - x)
                    if y > 0:
                        answer[i].add(x // y)
                if number in answer[i]:
                    return i + 1

    return -1
