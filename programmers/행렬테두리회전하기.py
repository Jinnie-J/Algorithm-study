def solution(rows, columns, queries):
    answer = []
    array = [[0] * columns for i in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            array[i][j] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1]
        min_value = tmp

        for k in range(x1 - 1, x2 - 1):
            test = array[k + 1][y1 - 1]
            array[k][y1 - 1] = test
            min_value = min(min_value, test)

        for k in range(y1 - 1, y2 - 1):
            test = array[x2 - 1][k + 1]
            array[x2 - 1][k] = test
            min_value = min(min_value, test)

        for k in range(x2 - 1, x1 - 1, -1):
            test = array[k - 1][y2 - 1]
            array[k][y2 - 1] = test
            min_value = min(min_value, test)

        for k in range(y2 - 1, y1 - 1, -1):
            test = array[x1 - 1][k - 1]
            array[x1 - 1][k] = test
            min_value = min(min_value, test)

        array[x1 - 1][y1] = tmp
        answer.append(min_value)

    return answer
