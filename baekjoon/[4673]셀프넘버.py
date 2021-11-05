arr = [0] * 10001

for i in range(1, 10001):
    number = i
    tmp = str(i)
    for j in range(len(tmp)):
        number += int(tmp[j])
    if (number) <= 10000:
        arr[number] = 1

for i in range(1, 10001):
    if arr[i] == 0:
        print(i)

# set 활용한 풀이
numbers = set(range(1, 10000))
remove_set = set()

for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num)

self_numbers = sorted(numbers - remove_set)
for i in self_numbers:
    print(i)
