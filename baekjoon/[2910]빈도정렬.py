n, c = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
for x in arr:
    if x not in dic:
        dic[x] = 0
    dic[x] += 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for x, y in dic:
    for z in range(y):
        print(str(x) + " ", end="")
