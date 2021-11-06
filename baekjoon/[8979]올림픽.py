n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
d = {}
d[arr[0][0]] = 1

for i in range(1, len(arr)):
    cnt = 0
    if arr[i - 1][1:4] == arr[i][1:4]:
        d[arr[i][0]] = d[arr[i - 1][0]]
    else:
        d[arr[i][0]] = len(d) + 1

print(d[k])
