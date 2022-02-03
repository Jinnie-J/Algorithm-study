# dfs 풀이 -> 무한루프 발생
def dfs(L, x):
    global answer
    print(L, x)
    if x > k:
        return
    if x == k:
        answer = min(answer, L)
    else:
        dfs(L + 1, x + 1)
        dfs(L + 1, x - 1)
        dfs(L + 1, x * 2)


n, k = map(int, input().split())
answer = 214700000
dfs(0, n)
print(answer)

# bfs 풀이 (가장 짧은, 가장 빠른 것을 구할 때)
from collections import deque

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            return dp[x]
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and not dp[i]:
                q.append(i)
                dp[i] = dp[x] + 1


n, k = map(int, input().split())
q = deque([n])
dp = [0] * (100001)
print(bfs())
