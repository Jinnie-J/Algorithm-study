
#안테나가 배열의 최솟값 위치 부터 최댓값 위치에 있는 모든 경우를 구한 방법 => 출력초과
n = int(input())
arr = list(map(int, input().split()))

minsum = sum(arr)
nowsum = 0
answer = 0

for i in range(min(arr), max(arr) + 1):
    nowsum = 0
    for house in arr:
        nowsum += abs(i - house)
    if nowsum < minsum:
        minsum = nowsum
        answer = i
print(answer)


#배열을 정렬 후, 그 중간 위치에 있는 경우 최소 거리를 구할 수 있다.
n= int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr[(n-1)//2])