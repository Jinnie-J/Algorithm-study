h, w = map(int, input().split())
for i in range(h):
    result = []
    arr = list(input())
    for j in range(len(arr)):
        cnt = 0
        if arr[j] == 'c':
            result.append(0)
        else:
            for k in range(j - 1, -1, -1):
                cnt += 1
                if arr[k] == 'c':
                    result.append(cnt)
                    break
            else:
                result.append(-1)
    for x in result:
        print(x, end=' ')
