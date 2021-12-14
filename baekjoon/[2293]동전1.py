n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

arr = [0] * (k + 1)
arr[0] = 1

for x in coins:
    for i in range(x, k + 1):
        arr[i] += arr[i - x]
print(arr[k])
