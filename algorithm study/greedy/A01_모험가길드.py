n = int(input())
stack = list(map(int, input().split()))

result = 0
stack.sort()
stackBreak = True

while len(stack) != 0:
    for i in range(stack[-1]):
        if len(stack) == 0:
            stackBreak = False
            break
        stack.pop()
    if not stackBreak:
        break
    result += 1

print(result)
