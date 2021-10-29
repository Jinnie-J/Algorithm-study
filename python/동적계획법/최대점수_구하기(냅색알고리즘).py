
#문제 하나 당 한 번 씩만 풀이 가능하기 때문에, 배열의 뒤 부터 채워 넣는다.
n, m = map(int, input().split())

ch = [0] * (m + 1)
for i in range(n):
    c, t = map(int, input().split())  #점수, 걸리는 시간
    for j in range(m,t-1,-1):
        ch[j] = max(ch[j], ch[j - t] + c)

print(ch[m])
