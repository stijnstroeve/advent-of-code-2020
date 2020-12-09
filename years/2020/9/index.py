lines = [int(x) for x in open("input.txt").read().split('\n')]
previous = 25


def check_sum(i, target):
    t_lines = lines[i:previous + i]

    for x in t_lines:
        for y in t_lines:
            if x + y == target and x != y:
                return True

    return False


def find_contiguous(target):

    z = 0
    while z < len(lines):
        for x in range(len(lines)):
            summed = []
            for f in range(z):
                if f + x > len(lines) - 1: continue
                summed.append(lines[f + x])

            if sum(summed) == target and summed[0] != target:
                return summed
        z += 1


t_i = 0
for i, line in enumerate(lines):
    if i < previous:
        continue

    if not check_sum(t_i, line):
        print('Part 1:', line)
        found = find_contiguous(line)

        x = min(found)
        y = max(found)

        print('Part 2:', x + y)
        break

    t_i += 1