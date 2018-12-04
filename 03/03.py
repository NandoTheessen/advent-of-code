from collections import defaultdict

def part1():
    C = defaultdict(int)

    for line in open('input.txt'):
        words = line.split()
        x,y = words[2].split(',')
        x,y = int(x), int(y[:-1])
        w, h = words[3].split('x')
        w, h = int(w), int(h)

        for dx in range(w):
            for dy in range(h):
                C[(x+dx, y+dy)] += 1

    for line in open('input.txt'):
        words = line.split()
        x,y = words[2].split(',')
        x,y = int(x), int(y[:-1])
        w, h = words[3].split('x')
        w, h = int(w), int(h)
        ok = True
        for dx in range(w):
            for dy in range(h):
                if C[(x+dx, y+dy)] > 1:
                    ok = False
        if ok:
            print words[0]

    ans = 0
    for (r, c), v in C.items():
        if v >= 2:
            ans += 1


    print("Overlapping square inches : {ans}".format(ans=ans))

part1()