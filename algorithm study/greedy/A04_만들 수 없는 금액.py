from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
arr = []

#배열의 값을 모두 더한 것 보다 한 개 더 큰 배열 생성(마지막 다음 수 까지 확인하기 위해)
for i in range(sum(nums) + 2):
    arr.append(0)

#모든 조합을 확인해서 값이 있는 배열을 1로 바꿔주기
for i in range(0, n + 1):
    combi = list(combinations(nums, i))
    for j in range(len(combi)):
        arr[sum(combi[j])] = 1

#첫 번째로 값이 0인 배열(조합이 없는 수) 출력
for i in range(len(arr)):
    if arr[i] == 0:
        print(i)
        break



# combinations를 사용하지 않은 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)
