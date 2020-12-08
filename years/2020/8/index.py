lines = [(x.split(' ')[0], int(x.split(' ')[1])) for x in open("input.txt").read().split('\n')]


def part1():

    accumulator = 0
    ran = []

    i = 0
    current_instruction = lines[0]

    while(current_instruction != None):
        [instruction, value] = current_instruction

        if instruction == 'acc':
            accumulator += value
            i += 1
        if instruction == 'jmp':
            i += value
        if instruction == 'nop':
            i += 1

        if i in ran:
            break

        ran.append(i)
        current_instruction = lines[i]

    return accumulator


def part2():

    def try_change(lines):
        accumulator = 0
        ran = []

        i = 0
        current_instruction = lines[0]
        has_double = False

        while(current_instruction != None):
            [instruction, value] = current_instruction

            if instruction == 'acc':
                accumulator += value
                i += 1
            if instruction == 'jmp':
                i += value
            if instruction == 'nop':
                i += 1

            if i in ran:
                has_double = True
                break

            ran.append(i)
            if i < len(lines):
                current_instruction = lines[i]
            else:
                break

        return has_double, accumulator

    for i, [instruction, value] in enumerate(lines):
        duped = lines.copy()
        if instruction == 'jmp':
            duped[i] = ('nop', value)
        if instruction == 'nop':
            duped[i] = ('jmp', value)

        [has_double, accumulator] = try_change(duped)
        if not has_double:
            return accumulator

    return 0


print('Part 1:', part1())
print('Part 2:', part2())