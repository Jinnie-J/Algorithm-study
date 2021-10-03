from collections import deque

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)

#현재 과목이 필수과목에 포함되어 있다면, 필수과목 큐의 첫번 째 인수여야 한다. 첫번 째 인수가 아니라면 NO
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
#for문이 break에 걸리지 않고 정상종료 되었으면, else문이 실행된다.
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))
