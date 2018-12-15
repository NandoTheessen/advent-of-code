from collections import deque

input = [0, 7, 7, 2, 0, 1]

e_one = input[0]
e_two = input[1]
position_one = 0
position_two = 1

for x in range(17):
    sum = e_one + e_two
    if sum > 10:
        new = [int(i) for i in str(sum)]
        input.append(int(new[0]))
        input.append(int(new[1]))
    else:
        input.append(sum)
    new_index_one = position_one + 1 + e_one
    new_index_two = position_two + 1 + e_two

    if (new_index_one) < (len(input)):
        e_one = input[new_index_one]
        position_one = new_index_one
    else:
        e_one = input[new_index_one-len(input)]
        position_one = new_index_one-len(input)

    if (new_index_two) < (len(input)):
        e_two = input[new_index_two]
        position_two = new_index_two
    else:
        e_two = input[new_index_two-len(input)]
        position_two = new_index_two-len(input)

    print(input)
    print("pos 1: ", position_one, "pos 2: ", position_two)


print(input)


recipes = '077201'
score = '37'
elf1 = 0
elf2 = 1
while recipes not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

print('Part 1:', score[int(recipes):int(recipes)+10])
print('Part 2:', score.index(recipes))
