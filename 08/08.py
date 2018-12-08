input = list(map(int, open('input.txt').readline().split()))

i = 0


def next_int():
    global i
    global input
    i += 1
    return input[i-1]


def read_tree():
    nc, nm = next_int(), next_int()
    children = []
    metadata = []
    for _ in range(nc):
        children.append(read_tree())
    for _ in range(nm):
        metadata.append(next_int())
    return (children, metadata)


def sum_metadata((children, metadata)):
    ans = 0
    for m in metadata:
        ans += m
    for c in children:
        ans += sum_metadata(c)
    return ans


def value((children, metadata)):
    if not children:
        return sum(metadata)
    else:
        ans = 0
        for m in metadata:
            if 1 <= m <= len(children):
                ans += value(children[m-1])
        return ans


root = read_tree()

print(sum_metadata(root))
print(value(root))
