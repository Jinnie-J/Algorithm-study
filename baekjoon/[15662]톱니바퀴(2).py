import copy

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
k = int(input())
rotArr = [list(map(int, input().split())) for _ in range(k)]

def rotate(arr, dir):
    if dir == 1:
        left = arr[:-1]
        right = arr[-1:]
    else:
        left = arr[:1]
        right = arr[1:]
    return right + left

tmpArr = copy.deepcopy(arr)

for x, y in rotArr:
    tmp = x - 1
    dir = y
    tmpArr[tmp] = rotate(tmpArr[tmp], dir)
    while tmp < n - 1:
        if tmpArr[tmp][2 + dir] != tmpArr[tmp + 1][6]:
            dir = -dir
            tmpArr[tmp + 1] = rotate(tmpArr[tmp + 1], dir)
            tmp += 1
        else:
            break

    tmp = x - 1
    dir = y
    while tmp > 0:
        if tmpArr[tmp][6 + dir] != tmpArr[tmp - 1][2]:
            dir = -dir
            tmpArr[tmp - 1] = rotate(tmpArr[tmp - 1], dir)
            tmp -= 1
        else:
            break
cnt = 0
for x in tmpArr:
    if x[0] == 1:
        cnt += 1
print(cnt)
