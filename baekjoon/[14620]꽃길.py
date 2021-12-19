n= int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

flower=[(0,0),(-1,0),(1,0),(0,-1),(0,1)]
visited=[[False]*n for _ in range(n)]
mincost = 987654321

def check(x,y):
    for dx,dy in flower:
        nx = x+dx
        ny = y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visited[nx][ny]:
            return False
    return True

def calculate(x,y):
    result = 0
    for dx,dy in flower:
        nx = x+dx
        ny = y+dy
        result +=arr[nx][ny]
    return result



def dfs(x,cost,cnt):
    global mincost
    if cnt==3:
        mincost = min(mincost , cost)
        return
    for i in range(x,n):
        for j in range(1,n):
            if check(i,j):
                visited[i][j]=True
                for dx,dy in flower:
                    visited[i+dx][j+dy]=True
                dfs(i,cost+calculate(i,j),cnt+1)
                visited[i][j]=False
                for dx,dy in flower:
                    visited[i+dx][j+dy]=False

dfs(1,0,0)
print(mincost)