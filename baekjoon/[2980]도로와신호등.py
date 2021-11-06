# 신호등 별로 시간의 경과만큼 대기시간을 담은 2차원 배열을 생성하여,
# 1초씩 시간을 더해가며 해당 위치에 신호등이 있으면, 현재시간에서의 대기시간을 각각 더해주었다.
n, L = map(int, input().split())
wait_time = []
location = []
for i in range(n):
    arr = [0] * (10001)
    d, r, g = map(int, input().split())
    location.append(d)
    red = r
    j = 0
    while j < 10001:
        arr[j] = red
        red -= 1
        if red == 0:
            for _ in range(g):
                j += 1
                if j < 10001:
                    arr[j] = 0
            red = r
        j += 1
    wait_time.append(arr)
j = 0
time = 0
for i in range(L + 1):
    time += 1
    if j < len(location) and i == location[j]:
        time += wait_time[j][time]
        j += 1

print(time)


# 간단하게 풀이한 코드 (현재시간, 빨간불, 초록불의 주기를 이용)
N, L = map(int, input().split())
pos = 0
answer = 0

for _ in range(N):
    d, r, g = map(int, input().split())

    answer += (d - pos)
    pos = d
    if answer % (r + g) <= r:
        answer += (r - (answer % (r + g)))

answer += (L - pos)
print(answer)
