# 몫과 나머지 이용한 풀이
n = int(input())
arr = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

max = -2147000000
for x in arr:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)


# 문자열 이용한 풀이
n = int(input())
arr = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000
for x in arr:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)
