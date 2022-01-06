def solution(genres, plays):
    total = {}
    d = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]] = [(plays[i], i)]
            total[genres[i]] = plays[i]
        else:
            d[genres[i]].append((plays[i], i))
            total[genres[i]] = total[genres[i]] + plays[i]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for x in total:
        arr = d[x[0]]
        arr = sorted(arr, key=lambda x: x[0], reverse=True)

        if len(arr) == 1:
            answer.append(arr[0][1])
        else:
            for i in range(2):
                answer.append(arr[i][1])
    return answer
