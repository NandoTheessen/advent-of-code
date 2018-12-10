import re
from collections import defaultdict


def update(points):
    result = []
    for x, y, vx, vy in points:
        result.append((x + vx, y+vy, vx, vy))
    return result


def display(points):
    x0 = min(x[0] for x in points)
    x1 = max(x[0] for x in points)
    y0 = min(x[1] for x in points)
    y1 = max(x[1] for x in points)

    rows = []
    p = set((x[0], x[1]) for x in points)
    for y in range(y0, y1+1):
        row = []
        for x in range(x0, x1+1):
            if (x, y) in p:
                row.append('X')
            else:
                row.append('.')
        rows.append(''.join(row))
    return '\n'.join(rows)


points = []
for line in open('input.txt'):
    x, y, vx, vy = map(int, re.findall(r'[-\d]+', line))
    points.append((x, y, vx, vy))

i = 0
while True:
    i += 1
    if abs(i - 10520) < 3:
        print(i)
        d = display(points)
        print(d)
    points = update(points)
