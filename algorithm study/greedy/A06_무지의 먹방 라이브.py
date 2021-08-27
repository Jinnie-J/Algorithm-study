
#효율성에서 탈락한 코드

food_times = list(map(int, input().split()))
k = int(input())
arr = []
n = sum(food_times)
while n > -1:
    for i in range(len(food_times)):
        if food_times[i] != 0:
            arr.append(i)
            food_times[i] -= 1
    n -= len(food_times)

print(arr[k] + 1)

#다시 풀어보기