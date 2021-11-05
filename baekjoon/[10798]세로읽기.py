arr = []
for i in range(5):
    arr.append(list(input()))

maxlen = 0
for i in range(5):
    maxlen = max(maxlen, len(arr[i]))

for i in range(5):
    while len(arr[i]) < maxlen:
        arr[i].append(0)

str = ""
for i in range(maxlen):
    for j in range(5):
        if arr[j][i] != 0:
            str += arr[j][i]
print(str)
