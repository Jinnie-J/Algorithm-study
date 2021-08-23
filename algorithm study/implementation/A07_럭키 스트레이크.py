arr = input()
a = 0
b = 0
for i in range(len(arr) // 2):
    a += int(arr[i])
for i in range(len(arr) // 2, len(arr)):
    b += int(arr[i])

if a == b:
    print("LUCKY")
else:
    print('READY')
