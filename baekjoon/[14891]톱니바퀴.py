from collections import deque

arr = []
for _ in range(4):
    arr.append(deque(list(map(int, input()))))

k = int(input())


def rotate(index, d):
    if d == 1:
        arr[index].insert(0, arr[index].pop())
    else:
        arr[index].append(arr[index].popleft())


for _ in range(k):
    index, dir = map(int, input().split())
    rotateArr = [[index - 1, dir]]

    x = index - 1
    nowdir = dir
    while x + 1 <= 3:
        if arr[x][2] != arr[x + 1][6]:
            nowdir = -nowdir
            rotateArr.append([x + 1, nowdir])
        else:
            break
        x += 1

    x = index - 1
    nowdir = dir
    while x - 1 >= 0:
        if arr[x][6] != arr[x - 1][2]:
            nowdir = -nowdir
            rotateArr.append([x - 1, nowdir])
        else:
            break
        x -= 1

    for x, dir in rotateArr:
        rotate(x, dir)

print(arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8)
