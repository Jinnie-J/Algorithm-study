def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]
    tmp = 1
    x = -1
    y = 0

    #방향 상,하,우
    for i in range(n):
        for j in range(i, n):
            #하
            if i % 3 == 0:
                x += 1
            #우
            elif i % 3 == 1:
                y += 1
            #상
            elif i % 3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = tmp
            tmp += 1
    for x in arr:
        for y in x:
            if y != 0:
                answer.append(y)

    return answer
