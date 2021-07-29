#'각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수'를 찾는다.

n,m= map(int,input().split())

result=0

for i in range(n):
    data=list(map(int,input().split()))
    #각 행에서 '가장 작은 수' 찾기
    min_value=min(data)

    #'가장 작은 수'들 중에서 가장 큰 수 찾기
    result=max(result,min_value)

print(result)