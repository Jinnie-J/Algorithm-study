from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

q = [i for i in range(1, n + 1)]
q = deque(q)

count = 0
for i in range(m):
    while True:
        if q[0] == arr[i]:
            q.popleft()
            break

        else:
            if q.index(arr[i]) < len(q) / 2:
                while q[0] != arr[i]:
                    q.append(q.popleft())
                    count += 1

            else:
                while q[0] != arr[i]:
                    q.appendleft(q.pop())
                    count += 1

print(count)
