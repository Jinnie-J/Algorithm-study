n = int(input())
note = []
for i in range(n):
    note.append(input())

words = []
for i in range(n - 1):
    words.append(input())

note.sort()
words.sort()

for i in range(n - 1):
    if note[i] != words[i]:
        print(note[i])
        break
else:
    print(note[n - 1])

# 딕셔너리 이용한 풀이
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n - 1):
    word = input()
    p[word] = 0
for key, val in p.items:
    if val == 1:
        print(key)
        break
