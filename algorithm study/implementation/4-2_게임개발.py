# 방향을 설정해서 이동하는 문제 유형애서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]

d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북,동,남,서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0


# 방향 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


while True:
    # 1.왼쪽으로 회전하기
    turn_left()
    # 2.회전해서 앞으로 이동한 칸이 갈 수 있는 칸(바다x, 가보지 않은 칸) 이면 앞으로 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    if array[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 3.이동할 수 없는 칸이면 왼쪽으로 한번 더 회전
    else:
        turn_time += 1
    # 4.모든 방향의 칸을 가지 못하면 뒤로 한칸 이동
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = nx
        # 5.뒤로 한칸 이동하지 못하는 상황이면 중단
        else:
            break
        turn_time = 0

print(count)
