
#팩토리얼의 0의 개수는 5가 곱해진 개수이다
#5로 나눈 몫과 5의 제곱수들로 나눈 몫을 더해준다.

import sys
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    cnt = 0
    j = 5
    while j <= num:
        cnt += num // j
        j *= 5
    print(cnt)