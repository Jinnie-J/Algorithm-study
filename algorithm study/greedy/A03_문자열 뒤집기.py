s = input()
#0으로 뒤집는 횟수
count0 = 0
#1으로 뒤집는 횟수
count1 = 0

#첫 번째 원소가 1이면 0으로 뒤집는 횟수 +1, 0이면 1으로 뒤집는 횟수 +1
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s) - 1):
    if s[i] == '0' and s[i + 1] == '1':
        count0 += 1
    if s[i] == '1' and s[i + 1] == '0':
        count1 += 1

print(min(count0, count1))
