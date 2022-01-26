def solution(s):
    answer = []
    tmp = []
    result = []
    arr = list(s)
    str = ""
    for i in range(len(arr)):
        #숫자일 때
        if 48 <= ord(arr[i]) <= 57:
            str += arr[i]
        # ',' 일 때
        elif ord(arr[i]) == 44 and ord(arr[i - 1]) != 125:
            tmp.append(str)
            str = ""
        # '}' 일 때
        elif ord(arr[i]) == 125:
            tmp.append(str)
            answer.append(tmp)
            str = ""
            tmp = []

    answer.pop()
    answer.sort(key=len)

    for x in answer:
        for y in x:
            if int(y) not in result:
                result.append(int(y))

    return result

# 간단한 풀이
def solution(s):
    answer = []

    s = s.lstrip('{').rstrip('}').split('},{')

    arr = []
    for x in s:
        arr.append(x.split(','))

    arr.sort(key=len)

    for x in arr:
        for y in x:
            if int(y) not in answer:
                answer.append(int(y))

    return answer
