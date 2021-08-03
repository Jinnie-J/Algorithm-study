#내가 작성한 코드
#plans 리스트에서 요소 하나씩 확인하여 한칸씩 이동해주기. N X N 범위를 벗어날 시 다시 원래 칸으로 이동

n= int(input())
x,y=1,1

plans= input().split()

for plan in plans:
    if plan =='R':
        x+=1
        if x==n+1:
            x-=1
    elif plan=='U':
        y-=1
        if y==0:
            y+=1
    elif plan=='L':
        x-=1
        if x==0:
            x+=1
    elif plan=='D':
        y+=1
        if y==n+1:
            y-=1

print(y,x,sep=' ')


#책에 있는 코드
#일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류되며 구현이 중요한 대표적인 문제 유형

n= int(input())
x,y=1,1
plans=input().split()

#L,R,U,D에 따른 이동 방향
dx= [0,0,-1,1]
dy= [-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or ny<1 or nx<n or ny>n:
        continue
    x,y=nx,ny

print(x,y)