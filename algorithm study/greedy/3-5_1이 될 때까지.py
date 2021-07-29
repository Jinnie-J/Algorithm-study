#주어진 N에 대하여 '최대한 많이 나누기'를 수행하면 된다.
#K가 2 이상의 수로 나누는 것이 1을 빼는 것보다 숫자를 훨씬 많이 줄일 수 있다.

n,k= map(int,input().split())
count=0

#N이 K 이상이라면 K로 계속 나누기
while n>=k:
    while n%k !=0:
        n-=1
        count+=1
    n//=k
    count+=1

#마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n-=1
    count+=1

print(count)