n = int(input())
for i in range(n):
    s = input()
    stack = []
    stack.append(s[0])

    for j in range(1, len(s)):
        if s[j] == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
