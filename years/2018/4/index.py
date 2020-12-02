from collections import Counter

lines = open("input.txt").read().split('\n')
output = open('output.txt', 'w+')

def part1():
    lines.sort()
    current_guard = 0
    sleeping_guards = {}
    sleeping_minutes = {}

    for line in lines:
        instruction = line.split(']')[1][1:]

        hour = int(line.split(':')[0][-2:])
        minute = int(line.split(':')[1][:2])

        if 'begins shift' in instruction:
            guard = int(instruction.split(' ')[1][1:])
            current_guard = guard

        if 'falls asleep' in instruction:
            sleeping_guards[current_guard] = minute

        if 'wakes up' in instruction:
            starting_min = sleeping_guards[current_guard]
            time_slept = minute - starting_min

            if current_guard not in sleeping_minutes:
                sleeping_minutes[current_guard] = []

            for i in range(time_slept):
                sleeping_minutes[current_guard].append(starting_min + i)

    highest_minutes = 0
    highest_guard = 0

    for x in sleeping_minutes.items():
        if len(x[1]) > highest_minutes:
            highest_minutes = len(x[1])
            highest_guard = x[0]

    items = Counter(sleeping_minutes[highest_guard]).most_common(1)
    return int(items[0][0]) * highest_guard


print('Part 1:', part1())