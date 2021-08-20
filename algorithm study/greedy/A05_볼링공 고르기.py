from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
# 두 개로 짝지을 수 있는 모든 조합을 구한 뒤, 두 값이 같은 경우의 수만 빼주었다
combi = list(combinations(arr, 2))

for i in range(len(combi)):
    if combi[i][0] == combi[i][1]:
        cnt += 1

print(len(combi) - cnt)



# combinations를 사용하지 않은 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
array = [0] * 11

for x in data:
    array[x] += 1

for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
