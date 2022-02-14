def solution(s):
    answer = 0

    arr = []
    arr.append(s[0])

    for i in range(1, len(s)):
        if arr and s[i] == arr[-1]:
            arr.pop()
        else:
            arr.append(s[i])

    if len(arr) == 0:
        answer = 1

    return answer


