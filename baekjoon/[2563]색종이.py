n = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1

answer = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            answer += 1

print(answer)
