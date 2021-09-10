# 유니코드 이용하여 숫자 확인
s = input()
num = ""
answer = []
for st in s:
    if ord(st) >= 40 and ord(st) <= 57:
        num += st

num = int(num)

for i in range(1, int(num ** (1 / 2)) + 1):
    if num % i == 0:
        answer.append(i)
        if (i ** 2) != num:
            answer.append(num // i)

print(num)
print(len(answer))

# isdecimal() 함수 이용
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)
