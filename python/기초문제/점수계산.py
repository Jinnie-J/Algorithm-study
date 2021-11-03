n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

if arr[0] == 1:
    answer[0] = 1
else:
    answer[0] = 0

for i in range(1, n):
    if arr[i] == 0:
        answer[i] = 0
    else:
        answer[i] = answer[i - 1] + 1

print(sum(answer))

# 다른 풀이
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
