r, b = map(int, input().split())
size = r + b
x = 3
while True:
    if size % x == 0:
        if (x - 2) * (size // x - 2) == b:
            print(max(x, size // x), min(x, size // x))
            break
    x += 1
