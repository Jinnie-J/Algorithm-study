
# re.split("\d+", string) : 문자열 속 연결된 숫자가 연속되어 출력 [12,3,45]
# re.split("\d", string) : 문자열 속 숫자가 한개씩 출력 [1,2,3,4,5]
import re

n = int(input())
arr = []

for i in range(n):
    for j in list(re.split("\D", str(input()))):
        if j != "": arr.append(int(j))

arr.sort()

for x in arr:
    print(x)
