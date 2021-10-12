def solution(record):
    answer = []
    nameDic = {}
    recordArr = []

    for i in range(len(record)):
        recordArr.append([])
        recordArr[i] = record[i].split()

    for i in range(len(recordArr)):
        if len(recordArr[i]) > 2:
            nameDic[recordArr[i][1]] = recordArr[i][2]

    for i in range(len(recordArr)):
        s = ""
        if recordArr[i][0] == 'Enter':
            s += nameDic[recordArr[i][1]] + ''
            s += '님이 들어왔습니다.'
            answer.append(s)
        elif recordArr[i][0] == 'Leave':
            s += nameDic[recordArr[i][1]] + ''
            s += '님이 나갔습니다.'
            answer.append(s)
    return answer
