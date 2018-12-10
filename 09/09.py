from collections import deque, defaultdict

input = open('input.txt').readline().split(' ')
p = int(input[0])
m = int(input[-2])

print(p, m)

# Found @
# https://www.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/ebepyc7


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    # deque starting w/ the 0th marble
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        # if our marble is a multiple of 23, add it to the players score
        # -> since the players are going in a cycle, using the modulo for
        # player #

        # rotate our "circle" aka deque 7 clockwise to pop the marble 7 to
        # the left of
        # the 23 multiplier & do NOT add the marble to the circle
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            # rotate one and insert our new marble!
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


print(play_game(p, m))
print(play_game(p, m*100))
