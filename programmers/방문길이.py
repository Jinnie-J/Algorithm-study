
def solution(dirs):
    visited = set()
    x = 0
    y = 0

    for d in dirs:
        if d == "U" and x < 5:
            visited.add(((x, y), (x + 1, y)))
            x += 1
        elif d == "L" and y > -5:
            visited.add(((x, y - 1), (x, y)))
            y -= 1
        elif d == "R" and y < 5:
            visited.add(((x, y), (x, y + 1)))
            y += 1
        elif d == "D" and x > -5:
            visited.add(((x - 1, y), (x, y)))
            x -= 1

    return len(visited)
