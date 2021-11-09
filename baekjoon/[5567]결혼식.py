n = int(input())
m = int(input())

friends = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1

answer = set()

for i in range(1, n + 1):
    if friends[1][i] == 1 or friends[i][1] == 1:
        answer.add(i)
        for j in range(1, n + 1):
            if (friends[i][j] == 1 or friends[j][i] == 1) and j != 1:
                answer.add(j)

print(len(answer))
