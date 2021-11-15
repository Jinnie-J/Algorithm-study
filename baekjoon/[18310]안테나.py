#완전탐색으로, 시간초과 발생한 코드
n = int(input())
house = list(map(int, input().split()))

minlocation = min(house)
maxlocation = max(house)

answer = 2147000000
for i in range(minlocation, maxlocation + 1):
    sumdis = 0
    for x in house:
        sumdis += abs(i - x)
    if sumdis < answer:
        answer = sumdis
        location = i

print(location)

#집의 위치를 정렬하여, 가장 가운데 집에 안테나를 설치할 때가 총 거리의 최솟값이 된다
n = int(input())
house = list(map(int, input().split()))

house.sort()

print(house[(n - 1) // 2])
