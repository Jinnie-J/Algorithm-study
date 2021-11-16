m = int(input())
for i in range(m):
    n = int(input())
    d = {}
    for j in range(n):
        a, b = input().split()
        if b in d:
            d[b] += 1
        else:
            d[b] = 1

    wearsum = 1
    for key in d:
        wearsum *= (d[key] + 1)

    print(wearsum - 1)
