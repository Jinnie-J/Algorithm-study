def solution(arr1, arr2):
    x = len(arr2[0])
    y = len(arr1)
    answer = []
    for i in range(y):
        list = []
        for j in range(x):
            number = 0
            for k in range(len(arr1[0])):
                a = arr1[i][k]
                b = arr2[k][j]
                number += a * b
            list.append(number)
        answer.append(list)
    return answer