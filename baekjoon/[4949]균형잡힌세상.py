while True:
    s = input()
    stack = []

    if s == '.':
        break
    for x in s:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            elif stack[-1] == '[':
                stack.pop()

        elif x == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            elif stack[-1] == '(':
                stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')
