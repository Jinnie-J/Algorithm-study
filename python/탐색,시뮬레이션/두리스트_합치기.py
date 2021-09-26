# 효율성 nlogn 의 코드(sort함수 사용)
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

result = arr1 + arr2

result.sort()
print(result)

# 효율성 n의 코드
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if arr1[p1] <= arr2[p2]:
        c.append(arr1[p1])
        p1 += 1
    else:
        c.append(arr2[p2])
        p2 += 1
if p1 < n:
    c += arr1[p1:]
if p2 < m:
    c += arr2[p2:]

print(c)
