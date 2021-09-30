
#이분탐색 문제

def Count(len):
    cnt=1
    ep=arr[0]
    for i in range(1,n):
        if arr[i]-ep>=len:
            cnt+=1
            ep=arr[i]

n, c = int(input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()
lt=1
rt=arr[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)