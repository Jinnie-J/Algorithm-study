from collections import deque

dq = deque([])

n, k = map(int, input().split())

for i in range(1, n + 1):
    dq.append(i)

while len(dq) > 1:
    for _ in range(k - 1):
        dq.append(dq.popleft())
    dq.popleft()

print(dq[0])
