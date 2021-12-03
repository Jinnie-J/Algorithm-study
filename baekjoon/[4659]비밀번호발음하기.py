arr = ['a', 'e', 'i', 'o', 'u']

while True:
    acceptable = True
    s = input()
    if s == 'end':
        break
    for x in s:
        if x in arr:
            break
    else:
        s = "<" + s + "> is not acceptable."
        print(s)
        continue

    cnt1 = 0
    cnt2 = 0
    for x in s:
        if x in arr:
            cnt1 += 1
            cnt2 = 0
        elif x not in arr:
            cnt2 += 1
            cnt1 = 0

        if cnt1 >= 3 or cnt2 >= 3:
            s = "<" + s + "> is not acceptable."
            print(s)
            acceptable = False
            break
    if acceptable == False:
        continue

    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            if s[i] != "e" and s[i] != "o":
                s = "<" + s + "> is not acceptable."
                print(s)
                break
    else:
        s = "<" + s + "> is acceptable."
        print(s)
