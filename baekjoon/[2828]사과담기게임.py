n, m = map(int, input().split())
j = int(input())
arr = []
for i in range(j):
    arr.append(int(input()))

left = 1
right = m

move = 0
for x in arr:
    if left <= x <= right:
        continue
    elif x < left:
        move += (left - x)
        right -= (left - x)
        left = x
    elif x > right:
        move += (x - right)
        left += (x - right)
        right = x

print(move)
