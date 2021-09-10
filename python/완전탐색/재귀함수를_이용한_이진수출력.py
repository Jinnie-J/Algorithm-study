def dfs(number):
    if number == 0:
        return
    else:
        arr.append(number % 2)
        dfs(number // 2)


arr = []
n = int(input())
dfs(n)
arr = arr[::-1]
print(arr)

print(''.join(map(str, arr)))
