# 정확성 수정필요
def solution(n, words):
    answer = []

    arr = []
    word_set = []
    for i in range(n):
        arr.append([])

    i = 0
    stop = False
    tmp = words[0][0]
    while i < len(words):
        for j in range(n):
            if words[i] in word_set or words[i][0] != tmp or len(words[i]) == 1:
                answer.append(j + 1)
                answer.append(len(arr[j]) + 1)
                stop = True
            else:
                arr[j].append(words[i])

            word_set.append(words[i])
            tmp = words[i][len(words[i]) - 1]
            i += 1

        if stop == True:
            break
    if len(answer) == 0:
        answer = [0, 0]

    return answer


# 간단한 코드
def solution(n, words):
    word_set = set([words[0]])
    tmp = words[0]

    for i in range(1, len(words)):
        if (tmp[-1] != words[i][0]) or words[i] in word_set:
            return [(i % n) + 1, (i // n) + 1]
        word_set.add(words[i])
        tmp = words[i]
    return [0, 0]
