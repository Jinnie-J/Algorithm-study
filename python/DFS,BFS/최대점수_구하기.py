def dfs(L,sum,time):
    global res
    if time>m:
        return
    if L==n:
        if sum > res:
            res=sum
    else:
        dfs(L+1, sum+pv[L],time+pt[L])
        dfs(L+1,sum,time)


n, m = map(int, input().split())
pv=list()
pt=list()

for _ in range(n):
    a,b = map(int, input().split())
    pv.append(a)
    pt.append(b)

res=-2147000000
dfs(0,0,0)
print(res)

