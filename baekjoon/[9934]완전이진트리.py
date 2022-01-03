import math
from collections import deque

n = int(input())
arr = list(map(int, input().split()))

result = []
lenArr = len(arr)
q = deque()

q.append(lenArr // 2)
k = int(math.pow(2, n - 2))
cnt = 1
num = 0
while q and num < n:
    tmpArr = []
    for i in range(cnt):
        tmp = q.popleft()
        tmpArr.append(arr[tmp])
        q.append(tmp - k)
        q.append(tmp + k)
    result.append(tmpArr)
    cnt *= 2
    num += 1
    k = k // 2

for x in result:
    for y in x:
        print(y, end=' ')
    print()
