n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
i = 0
sum = 0
sumcnt = 0
while i < n:
    sum += a[i]
    if sum == m:
        sum = 0
        cnt += 1
        i += 1
        i -= sumcnt
        sumcnt = 0
    elif sum > m:
        sum = 0
        i += 1
        i -= sumcnt
        sumcnt = 0
    else:
        i += 1
        sumcnt += 1
print(cnt)

# 가독성 좋게 바꾼 코드
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
total = a[0]
cnt = 0
while True:
    if total < m:
        if rt < n:
            total += a[rt]
            rt += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= a[lt]
        lt += 1
    else:
        total -= a[lt]
        lt += 1
print(cnt)
