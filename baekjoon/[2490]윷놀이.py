for i in range(3):
    a = 0
    b = 0
    arr = list(map(int, input().split()))
    for j in range(4):
        if arr[j] == 0:
            a += 1
        else:
            b += 1
    if a == 4:
        print('D')
    elif b == 4:
        print('E')
    elif a == 3 and b == 1:
        print('C')
    elif a == 2 and b == 2:
        print('B')
    else:
        print('A')
