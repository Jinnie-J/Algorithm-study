n, k = map(int, input().split())
index = 0
answer = 0
# index가 k가 될 때 까지 1부터 약수 찾기
for i in range(1, n + 1):
    if n % i == 0:
        index += 1
    if index == k:
        answer = i
        break
# if문에 걸리지 않으면 -1 출력
else:
    answer = -1

print(answer)
