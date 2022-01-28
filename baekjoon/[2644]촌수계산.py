import sys
sys.setrecursionlimit(300000)

def dfs(v):
    visited[v] = True
    for i in family[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

n = int(input())
a, b = map(int, input().split())
number = int(input())

family = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = [0] * (n + 1)

for i in range(number):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

dfs(a)

if res[b] > 0:
    print(res[b])
else:
    print(-1)
