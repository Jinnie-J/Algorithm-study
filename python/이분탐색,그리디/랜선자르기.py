def Count(length):
    cnt = 0
    for x in arr:
        cnt += x // length
    return cnt


k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

lt = 1
rt = max(arr)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) < n:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1

print(res)
