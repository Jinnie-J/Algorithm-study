data = input()
result = []
value = 0

#리스트의 원소가 알파벳이면 새로운 배열에, 숫자면 숫자끼리 더해주기
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))
