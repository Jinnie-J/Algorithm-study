#냅색 알고리즘 사용
n, m = map(int, input().split())
dy = [0] * (m + 1)

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m + 1):
        dy[i] = max(dy[i], dy[j - w] + v)
    print(dy[m])
