n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print(arr.index(m) + 1)

# 검색 범위를 좁혀 효율적이게 풀이한 코드
n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
lt = 0
rt = n - 1

while lt <= rt:
    mid = lt + rt // 2
    if arr[mid] == m:
        print(mid + 1)
        break
    elif arr[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
