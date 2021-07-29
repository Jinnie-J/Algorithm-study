#입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
#연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복하면 된다.

n,m,k = map(int, input().split())
data=list(map(int,input().split()))

data.sort()

result=0

while True:
    #가장 큰 수를 K번 더하기
    for i in range(k):
        if m==0:
            break
        result+=data[n-1]
        m-=1
    if m==0:
        break
    #두 번째로 큰 수를 한 번 더하기
    result+=data[n-2]
    m-=1

print(result)
