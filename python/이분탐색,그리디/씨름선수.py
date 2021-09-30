
n= int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[0], reverse=True)

cnt=n
for i in range(1,n):
    for j in range(i):
        if arr[i][1]<arr[j][1]:
            cnt-=1
            break

print(cnt)


#반복문 한단계 코드
n = int(input())
body=[]
for i in range(n):
    h,w = map(int,input().split())
    body.append((h,w))

body.sort(reverse=True)
largest=0
cnt=0

for x,y in body:
    if y>largest:
        largest=y
        cnt+=1
