from itertools import permutations


def operation(num1, num2, operator):
    if operator == '+':
        return str(int(num1) + int(num2))
    if operator == '-':
        return str(int(num1) - int(num2))
    if operator == '*':
        return str(int(num1) * int(num2))


def calculate(expression, operator):
    array = []
    tmp = ""
    for x in expression:
        if ord(x) == 43 or ord(x) == 42 or ord(x) == 45:
            array.append(tmp)
            array.append(x)
            tmp = ""
        else:
            tmp += x
    array.append(tmp)

    for op in operator:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == op:
                stack.append(operation(stack.pop(), array.pop(0), op))
            else:
                stack.append(tmp)
        array = stack

    return abs(int(array[0]))


def solution(expression):
    operator = ['+', '-', '*']
    operator = list(permutations(operator, 3))
    answer = []
    # (+,-,*) (+,*,-) (-,+,*) (-,*,+) (*,+,-) (*,-,+)의 순열
    for x in operator:
        answer.append(calculate(expression, x))
    return max(answer)
