n = int(input())
answer = []

for i in range(n):
    arr = []
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr = arr[s - 1:e]
    arr.sort()
    answer.append(arr[k - 1])
    print("#%d %d" % (i + 1, arr[k - 1]))
