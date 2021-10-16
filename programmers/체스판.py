# 주변 체스판 8개의 좌표를 확인하여 0~8범위를 넘어가지 않는 경우 answer +1 해준다
def solution(pos):
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, -2, 2, 1, -1, -1, 1]

    cx = ord(pos[0]) - ord("A")
    cy = ord(pos[1]) - ord("0") - 1

    answer = 0

    for i in range(8):
        xx = cx + dx[i]
        yy = cy + [dy[i]]
        if 0 <= xx < 8 and 0 <= yy < 8:
            answer += 1
    return answer
