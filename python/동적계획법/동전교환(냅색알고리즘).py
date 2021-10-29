n = int(input())
coins = list(map(int, input().split()))
m = int(input())
arr = [1000] * (m + 1)
arr[0] = 0

for i in range(n):
    for j in range(coins[i], m + 1):
        arr[j] = min(arr[j], arr[j - coins[i]] + 1)
print(arr[m])
