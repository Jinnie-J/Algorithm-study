# 시간초과 발생 코드1
n, m = map(int, input().split())
arr = [input() for _ in range(n)]

for i in range(m):
    tmp = input()
    if 48 <= ord(tmp[0]) <= 57:
        print(arr[int(tmp) - 1])
    else:
        print(arr.index(tmp) + 1)

# 시간초과 발생 코드2
n, m = map(int, input().split())

name = []
d = {}
for i in range(n):
    tmp = input()
    name.append(tmp)
    d[tmp] = i + 1

for _ in range(m):
    str = input()
    if 48 <= ord(str[0]) <= 57:
        print(name[int(str) - 1])
    else:
        print(d[str])

# 성공 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
d = {}
for i in range(n):
    tmp = input().rstrip()
    name.append(tmp)
    d[tmp] = i + 1

for _ in range(m):
    str = input().rstrip()
    if str.isdigit():
        print(name[int(str) - 1])
    else:
        print(d[str])
