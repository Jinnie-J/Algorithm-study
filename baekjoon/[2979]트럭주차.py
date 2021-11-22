a, b, c = map(int, input().split())
arr = []
maxval = 0
for i in range(3):
    s, e = map(int, input().split())
    arr.append([s, e])
    if e > maxval:
        maxval = e
answer = [0] * (maxval)

for i in range(3):
    for j in range(arr[i][0], arr[i][1]):
        if answer[j] == 0:
            answer[j] = a
        elif answer[j] == a:
            answer[j] = (b * 2)
        elif answer[j] == (b * 2):
            answer[j] = (c * 3)

print(sum(answer))
