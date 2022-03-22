def solution(n, words):
    answer = []
    whole_word = []
    p_word = []

    for _ in range(n):
        p_word.append([])

    i = 0
    while i < len(words):
        for j in range(n):
            if i > 0:
                if (words[i] in whole_word) or (words[i][0] != words[i - 1][-1]):
                    answer.append(j + 1)
                    answer.append(len(p_word[j]) + 1)
                    return answer

            p_word[j].append(words[i])
            whole_word.append(words[i])
            i += 1

    return [0, 0]


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
