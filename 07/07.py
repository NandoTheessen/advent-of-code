from collections import defaultdict, deque

E = defaultdict(list)
D = defaultdict(int)
def part_one():
    for line in open('input.txt'):
        words = line.split()
        x = words[1]
        y = words[7]
        E[x].append(y)
        D[y] += 1

    Q = []
    for k in E:
        if D[k] == 0:
            Q.append(k)

    ans = ""
    while Q:
        x = sorted(Q)[0]
        Q = [y for y in Q if y!=x]
        ans += x
        for y in E[x]:
            D[y] -= 1
            if D[y] == 0:
                Q.append(y)

    return ans


for line in open('input.txt'):
    words = line.split()
    x = words[1]
    y = words[7]
    E[x].append(y)
    D[y] += 1


for k in E:
    E[k] = sorted(E[k])

t = 0
EV = []
Q = []

def add_task(x):
    Q.append(x)      
    
def start_work():
    global Q
    while len(EV) < 5 and Q:
        x = min(Q)
        Q = [y for y in Q if y!=x]
        EV.append((t+61+ord(x) - ord('A'), x))

for k in E:
    if D[k] == 0:
        add_task(k)
        
start_work()

while EV or Q:
    t, x = min(EV)
    EV = [y for y in EV if y!=(t, x)]
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            add_task(y)
    start_work()

print t


print(part_one())
