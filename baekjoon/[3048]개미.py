#딕셔너리에 두 개미의 방향을 지정해주고, 방향이 다른 개미를 만났을 때, 위치를 변경해준다 (t번 반복).
n1, n2 = map(int, input().split())
ant1 = list(input())
ant2 = list(input())
t = int(input())

d = {}
for i in range(n1):
    d[ant1[i]] = 0
for i in range(n2):
    d[ant2[i]] = 1
ant1.reverse()
ant1.extend(ant2)

for _ in range(t):
    i = 0
    while i < len(ant1) - 1:
        if d[ant1[i]] == 0 and d[ant1[i + 1]] == 1:
            ant1[i], ant1[i + 1] = ant1[i + 1], ant1[i]
            i += 1
        i += 1

for x in ant1:
    print(x, end='')
