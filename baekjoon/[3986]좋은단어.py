n = int(input())
cnt = 0

for j in range(n):
    s = input()
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack:
            tmp = stack.pop()
            if tmp != s[i]:
                stack.append(tmp)
                stack.append(s[i])
        else:
            stack.append(s[i])

    if not stack:
        cnt += 1

print(cnt)
