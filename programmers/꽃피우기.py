
def solution(garden):

    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    arr = []
    while len(arr) < len(garden) ** 2:
        arr = []
        for i in range(len(garden)):
            for j in range(len(garden)):
                if garden[i][j] == 1:
                    arr.append([i, j])
                if len(arr) == len(garden) ** 2:
                    return answer
        for i in arr:
            for j in range(4):
                x = i[0] + dx[j]
                y = i[1] + dy[j]
                if 0 <= x <= len(garden) - 1 and 0 <= y <= len(garden) - 1:
                    garden[x][y] = 1
        answer += 1

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1,1],[1,1]]
ret2 = solution(garden2)

print("solution 함수의 반환 값은", ret2, "입니다.")
