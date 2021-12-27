n = int(input())

sign = list(map(str, input().split()))
visited = [False] * 11
minR = ""
maxR = ""


def poss(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j


def sol(d, s):
    global minR, maxR

    if d == n + 1:
        if len(minR) == 0:
            minR = s
        else:
            maxR = s
        return

    for i in range(10):
        if not visited[i]:
            if d == 0 or poss(s[len(s) - 1], str(i), sign[d - 1]):
                visited[i] = True
                sol(d + 1, s + str(i))
                visited[i] = False


sol(0, "")
print(maxR)
print(minR)