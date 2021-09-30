
# 성공했지만, 시간초과 난 코드
n= int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[0])

dy=[0]*n
dy[0]=1
for i in range(1,n):
    res=0
    for j in range(i):
        if arr[j][1]<=arr[i][0]:
            if dy[j]>res:
                res=dy[j]
    dy[i]=res+1

print(max(dy))


# 제일 먼저 끝나는 회의부터 시작해야 제일 많은 회의를 할 수 있다.
n= int(input())
metting=[]
#튜플형식으로 저장
for i in range(n):
    s, e = map(int,input().split())
    metting.append((s,e))
metting.sort(key= lambda x:(x[1],x[0]))

end_time=0
cnt=0
for s, e in metting:
    if s>=end_time:
        end_time=e
        cnt+=1
print(cnt)