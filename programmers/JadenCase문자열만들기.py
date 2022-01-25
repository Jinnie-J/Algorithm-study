def solution(s):
    answer = ''
    arr = s.split(' ')

    for x in arr:
        if x != '':
            first = x[0]
            left = x[1:]
            answer += first.upper()
            answer += left.lower()
        answer += ' '

    answer = answer[:len(answer) - 1]
    return answer
