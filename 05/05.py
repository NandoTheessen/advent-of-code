

string = open('input.txt').read()
alpha = 'abcdefghijklmnopqrstuvwxyz'

M = {}
for c in alpha:
    M[c.lower()] = c.upper()
    M[c.upper()] = c.lower()

def partOne():
    stack = []
    for c in string:
        if stack and c == M[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)

    return len(stack)

def partTwo():
    ans = 1000000
    stack = []
    for rem in alpha:
        s2 = [c for c in string if c!=rem.lower() and c!=rem.upper()]
        stack = []
        for c in s2:
            if stack and c == M[stack[-1]]:
                stack.pop()
            else:
                stack.append(c)

        ans = min(ans, len(stack))
    return ans



print("P1 :",partOne())

print("P2 :",partTwo())