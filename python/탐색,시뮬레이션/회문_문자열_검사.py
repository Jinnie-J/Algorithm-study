n = int(input())

for i in range(n):
    s = input()
    yes = 0
    for j in range(len(s) // 2):
        if s[j].lower() == s[len(s) - j - 1].lower():
            yes += 1
    if yes == len(s) // 2:
        print("#%d %s" % (i + 1, "YES"))
    else:
        print("#%d %s" % (i + 1, "NO"))

# 다른 문자열이 있을 때 break 를 통해 빠르게 빠져나오게 해주는 코드
n = int(input())

for i in range(n):
    s = input()
    for j in range(len(s) // 2):
        if s[j].lower() != s[len(s) - j - 1].lower():
            print("#%d %s" % (i + 1, "NO"))
            break
        else:
            print("#%d %s" % (i + 1, "YES"))

# 입력받은 문자가 문자열을 뒤집었을 때와 일치하는 경우, 회문 문자열이다
n = int(input())

for i in range(n):
    s = input()
    for j in range(len(s) // 2):
        if s == s[::-1]:
            print("#%d %s" % (i + 1, "YES"))
        else:
            print("#%d %s" % (i + 1, "NO"))
