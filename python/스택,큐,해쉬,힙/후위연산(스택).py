s = input()
stack = []

for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        s1 = stack.pop()
        s2 = stack.pop()
        if x == '+':
            stack.append(s1 + s2)
        elif x == '-':
            stack.append(s2 - s1)
        elif x == '*':
            stack.append(s1 * s2)
        else:
            stack.append(s2 / s1)

print(stack[0])
