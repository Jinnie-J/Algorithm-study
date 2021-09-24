def dfs(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j] + 64), end=' ')
        print()
    else:
        #알파벳 A~Z까지 탐색하여 일치하는 경우 배열에 추가해준다. 한 자리 수 인 경우 배열에 추가 후, 다음 수 탐색 & 두자리 수 인 경우 배열에 추가 후, 두 칸 뒤의 수 탐색
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                dfs(L + 1, P + 1)
            elif i >= 10 and i // 10 == code[L] and i % 10 == code[L + 1]:
                res[P] = i
                dfs(L + 2, P + 1)


code = list(map(int, input()))
n = len(code)
code.insert(n, -1)
res = [0] * n
cnt = 0
dfs(0, 0)
print(cnt)
