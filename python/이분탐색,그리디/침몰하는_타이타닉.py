n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

while arr:
    if len(arr) == 1:
        arr.pop()
        answer += 1
        break
    else:
        if arr[0] + arr[len(arr) - 1] > m:
            arr.pop()
            answer += 1
        else:
            arr.pop(0)
            arr.pop()
            answer += 1
print(answer)

# deque 이용한 풀이 (pop(0) 대신 popleft() 사용하여 효율성 증가)
from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)
answer = 0
while arr:
    if len(arr) == 1:
        answer += 1
        break
    else:
        if arr[0] + arr[-1] > m:
            arr.pop()
            answer += 1
        else:
            arr.popleft()
            arr.pop()
            answer += 1
print(answer)
