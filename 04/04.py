from collections import defaultdict

def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])

def argmax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

    
lines = open('input.txt').read().split('\n')
lines.sort()
C = defaultdict(int)
CM = defaultdict(int)

guard = None
asleep = None

for line in lines:
    time = parseTime(line)
    if 'begins shift' in line: 
        guard = int(line.split()[3][1:])
        asleep = None
    elif 'falls asleep' in line:
        asleep = time
    elif 'wakes up' in line:
        for t in range(asleep, time):
            CM[(guard,t)] +=1 # change to [guard][t] for solution of the first part
            C[guard] +=1
        asleep = False



best_guard, best_min = argmax(CM)

# change to best_guard = argmax(C) for solution of part 1

answer = best_guard * best_min

print answer