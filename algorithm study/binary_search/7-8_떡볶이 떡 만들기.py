n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 잘랐을 때 총 길이 구하기
    for x in array:
        if x > mid:
            total += x - mid
    #총 길이가 짧으면 더 많이 자르기
    if total < m:
        end = mid - 1
    #총 길이가 충분하면 덜 자르기
    else:
        result = mid
        start = mid + 1

print(result)
