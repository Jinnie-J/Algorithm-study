dicA = {}
dicB = {}

a = list(input())
b = list(input())
for i in range(len(a)):
    if a[i] in dicA:
        dicA[a[i]] += 1
    else:
        dicA[a[i]] = 1

for i in range(len(b)):
    if b[i] in dicB:
        dicB[b[i]] += 1
    else:
        dicB[b[i]] = 1
for i in range(len(a)):
    if a[i] not in dicB or dicA[a[i]] != dicB[a[i]]:
        print("NO")
        break
else:
    print("YES")

# 간단한 딕셔너리 생성 코드
a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
