arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for _ in range(10):
    a, b = map(int, input().split())
    tmp = arr[a - 1:b]
    tmp = tmp[::-1]
    cnt = 0
    for j in range(a - 1, b):
        arr[j] = tmp[cnt]
        cnt += 1

for x in arr:
    print(x, end=' ')

# 배열의 위치를 바꿔서 해결한 풀이
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]

a.pop()
for x in a:
    print(x, end=' ')
