
n = int(input())
arr= list(map(int,input().split()))
cnt= int(input())

for i in range(cnt):
    largest = arr.index(max(arr))
    smallest = arr.index(min(arr))
    
    arr[largest]-=1
    arr[smallest]+=1

print(max(arr)-min(arr))

#index함수 사용하지 않은 코드
n = int(input())
arr= list(map(int,input().split()))
cnt= int(input())
arr.sort()

for _ in range(cnt):
    arr[0]+=1
    arr[n-1]-=1
    arr.sort()

print(arr[n-1]-arr[0])
