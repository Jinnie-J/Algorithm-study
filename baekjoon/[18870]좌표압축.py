# 시간초과
# list.index(i)의 형태는 시간복잡도 O(N)을 가지고 있고 그렇다면 매번 최대 1,000,000번의 수행이 이루어지게 되어서 시간초과가 난다.
n = int(input())
arr = list(map(int, input().split()))

newarr = set(arr)
newarr = sorted(newarr)

answer = []
for n in arr:
    answer.append(newarr.index(n))

for i in answer:
    print(i, end=' ')

# 파이썬의 딕셔너리 이용 - 시간 복잡도 O(1)
# 딕셔너리 이름 = {"key값":"value값"} , key는 중복 허용 x

n = int(input())
arr = list(map(int, input().split()))

newarr = set(arr)
newarr = sorted(newarr)

dic = {newarr[i]: i for i in range(len(newarr))}

for i in arr:
    print(dic[i], end=' ')
