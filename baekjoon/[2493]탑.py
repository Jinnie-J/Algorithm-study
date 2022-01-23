# 시간초과 발생 코드
n = int(input())
arr = list(map(int, input().split()))

answer = []

for i in range(len(arr) - 1, 0, -1):
    wall = False
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[i]:
            answer.append(j + 1)
            wall = True
            break
    if wall == False:
        answer.append(0)

answer.append(0)
answer.reverse()

for x in answer:
    print(x, end=' ')

# 수정 코드 (스택 이용)
n= int(input())
arr = list(map(int,input().split()))

stack= []
answer = [0 for i in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > arr[i]:
            answer[i]=stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append([i,arr[i]])
print(*answer)
