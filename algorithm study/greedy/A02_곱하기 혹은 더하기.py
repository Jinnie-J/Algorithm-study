n = input()
arr = list(n)

for i in range(len(arr)):
    arr[i] = int(arr[i])

sum = arr[0]

for i in range(1, len(arr)):
    if arr[i] == 0 or sum == 0:
        sum += arr[i]
    else:
        sum *= arr[i]
print(sum)
