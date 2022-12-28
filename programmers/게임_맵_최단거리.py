# DFS 풀이 - 효율성 테스트 실패
def solution(maps):
    n = len(maps)  
    m = len(maps[0])
    
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    result=[]
    def dfs(x,y, sum_distance,visited):
        if x == n-1 and y == m-1:
            result.append(sum_distance)
            return
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                dfs(nx,ny,sum_distance + 1,visited)
                visited[nx][ny]=0
    
    answer = n*m
    visited=[[0]*n for _ in range(m)]
    dfs(0,0,1, visited)
    
    if result:
        return min(result)
    return -1

# BFS 풀이 - 성공
from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q=deque()
    q.append([0,0])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y]+1
                q.append([nx,ny])

    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1] 

