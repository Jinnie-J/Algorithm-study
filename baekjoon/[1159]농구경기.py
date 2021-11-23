n = int(input())
arr = []
for i in range(n):
    arr.append(input())

d = {}
for x in arr:
    if x[0] in d:
        d[x[0]] += 1
    else:
        d[x[0]] = 1

answer = []
for x in d:
    if d[x] >= 5:
        answer.append(x)

if len(answer) == 0:
    print("PREDAJA")
else:
    answer.sort()
    for x in answer:
        print(x, end='')
