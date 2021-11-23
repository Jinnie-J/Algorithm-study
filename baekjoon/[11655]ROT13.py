s = input()
answer = []
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        tmp = ord(s[i]) + 13
        if tmp > 90:
            tmp -= 26
        answer.append(chr(tmp))
    elif 97 <= ord(s[i]) <= 122:
        tmp = ord(s[i]) + 13
        if tmp > 122:
            tmp -= 26
        answer.append(chr(tmp))
    else:
        answer.append(s[i])

for x in answer:
    print(x, end='')
