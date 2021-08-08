n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    if b[i] in a:
        print('yes', end=' ')
    else:
        print('no', end=' ')


#이진 탐색으로 풀이한 코드
def binary_search(array, target, start, end):
    while start <= end:
        mid= (start+end) // 2
        if target==array[mid]:
            return mid
        elif target > array[mid]:
            start= mid+1
        else:
            end=mid-1
    return None

n= int(input())
a= list(map(int, input().split()))
m= int(input())
b= list(map(int, input().split()))

for i in b:
    result= binary_search(a,i,0,n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
