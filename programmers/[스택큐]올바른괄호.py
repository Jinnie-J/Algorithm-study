def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
    if len(stack) != 0:
        return False

    return True


# 간단한 풀이
def solution(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == "(" else x - 1 if w == ")" else x
    return x == 0
