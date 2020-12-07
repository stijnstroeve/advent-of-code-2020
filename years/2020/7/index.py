lines = open("input.txt").read().split('\n')


def get_parents(key):

    for line in lines:
        if 'no other' in line:
            continue

        current_bag = " ".join(line.split(' ')[:2])

        if current_bag != key:
            continue

        parents = [(int(x.replace('.', '').replace(' bags', '').replace(' bag', '').split(' ')[0]),
                    " ".join(x.replace('.', '').replace(' bags', '').replace(' bag', '').split(' ')[1:])) for x in
                   line.split('contain ')[1].split(', ')]

        return parents

    return []


def has_shiny_gold_parent(key, parent):

    if key[1] == 'shiny gold':
        return True


    parents = get_parents(key[1])


    if len(parents) > 0:
        for parent in parents:
            has_shiny_parent = has_shiny_gold_parent(parent, key)
            if has_shiny_parent == True:
                return True

    else:
        return False


def part1():
    p_map = {}
    c = 0
    for line in lines:
        print('new line', c)
        c += 1
        if 'no other' in line:
            continue

        current_bag = " ".join(line.split(' ')[:2])

        parents = [(int(x.replace('.', '').replace(' bags', '').replace(' bag', '').split(' ')[0]), " ".join(x.replace('.', '').replace(' bags', '').replace(' bag', '').split(' ')[1:])) for x in line.split('contain ')[1].split(', ')]

        for parent in parents:
            if parent[1] == 'shiny gold':
                p_map[current_bag] = 1
                c += 1

                continue

            if has_shiny_gold_parent(parent, ''):
                p_map[current_bag] = 1

    return len(list(p_map))


def part2():

    def reverse_search(key):
        parents = get_parents(key)

        count = 1
        for parent in parents:
            for c in range(parent[0]):
                count += reverse_search(parent[1])

        return count

    return reverse_search('shiny gold') - 1


print('Part 1', part1())
print('Part 2', part2())