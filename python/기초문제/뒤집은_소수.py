#에레토스테네스 체 소수판별 풀이 코드
def reverse(x):
    str=""
    strArr= list(x+"")
    for i in range(len(strArr)-1,-1,-1):
        str+=strArr[i]
    return int(str)


def isPrime(x):
    a= [True]*(x+1)
    a[0]=False
    a[1]=False
    for i in range(2,x+1):
        if a[i]:
            for j in range(i*2, x+1, i):
                a[j]=False
    if a[x]:
        return True
    else:
        return False

n= int(input())
arr = list(map(int,input().split()))
answer=[]

for i in range(len(arr)):
    if isPrime(reverse(arr[i])):
        answer.append(reverse(arr[i]))

for i in range(len(answer)):
    print(answer[i], end=' ')


#기본 소수판별 풀이 코드
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True

n= int(input())
a = list(map(int,input().split()))
for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
