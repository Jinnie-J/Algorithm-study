from math import floor


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            s1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            s2.append(str2[i:i + 2])

    cnt1, cnt2 = 0, 0
    for i in range(len(s1)):
        j = 0
        while j < len(s2):
            if s1[i] == s2[j]:
                s2.pop(j)
                cnt1 += 1
                break
            j += 1
    cnt2 = len(s1) + len(s2)

    if cnt1 == 0 and cnt2 == 0:
        return 65536
    return floor((cnt1 / cnt2) * 65536)
