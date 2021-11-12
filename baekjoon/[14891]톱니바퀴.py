arr = [list(map(int, input())) for _ in range(4)]
k = int(input())


def rot(index, d):
    if d == 1:
        l = arr[index][:-1]
        r = arr[index][-1:]
        arr[index] = r + l

    else:
        r = arr[index][:1]
        l = arr[index][1:]
        arr[index] = l + r


for i in range(k):
    a, b = map(int, input().split())

    rot(a - 1, b)

    left = a - 1
    right = a - 1
    direction = b
    while left > 0:
        left -= 1
        if arr[left][3] != arr[left + 1][7]:
            if direction == 1:
                direction = -1
            else:
                direction = 1
            rot(left, direction)

    direction = b
    while right < 3:
        right += 1
        if arr[right][7] != arr[right - 1][3]:
            if direction == 1:
                direction = -1
            else:
                direction = 1
            rot(right, direction)

answer = 0
score = 1
for i in range(4):
    if arr[i][0] == 1:
        answer += score
    score *= 2

print(answer)
