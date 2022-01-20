def solution(id_list, report, k):
    id_list_dic = {}
    cnt_dic = {}
    reportArr = []

    for i in range(len(id_list)):
        id_list_dic[id_list[i]] = 0

    report = set(report)
    report = list(report)

    for i in range(len(report)):
        reportArr.append([])
        reportArr[i] = report[i].split()

    for i in range(len(reportArr)):
        if reportArr[i][1] in cnt_dic:
            cnt_dic[reportArr[i][1]] += 1
        else:
            cnt_dic[reportArr[i][1]] = 1

    value = list(cnt_dic.values())
    key = list(cnt_dic.keys())

    for i in range(len(key)):
        if value[i] >= k:
            for x in reportArr:
                if x[1] == key[i]:
                    id_list_dic[x[0]] += 1
    answer = list(id_list_dic.values())

    return answer
