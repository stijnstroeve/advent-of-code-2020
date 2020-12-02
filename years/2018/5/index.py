global_chain = open("input.txt").read()


def react_chain(chain):
    chain = list(chain)

    amount_changed = 0

    for i, char in enumerate(chain):

        next_char_i = i + 1
        if next_char_i < len(chain):
            next_char = chain[next_char_i]

            is_same = next_char.lower() == char.lower()

            if (char.islower() & next_char.isupper() | char.isupper() & next_char.islower()) & is_same:
                chain[i] = '*'
                chain[next_char_i] = '*'

                amount_changed += 1

    chain = "".join(chain)

    chain = chain.replace('*', '')

    return chain, amount_changed


def full_react_chain(chain):
    total_changed = -1
    while total_changed != 0:
        new_chain = react_chain(chain)
        total_changed = new_chain[1]
        chain = new_chain[0]

    return chain


def part1(chain):

    chain = full_react_chain(chain)

    output = open('chain1.txt', 'w+')
    output.write(chain)

    return len(chain)


def part2(chain):

    abet = 'abcdefghijklmnopqrstuvwxyz'
    abet_map = {}

    for char in abet:
        test_chain = chain.replace(char, '').replace(char.upper(), '')
        new_chain = full_react_chain(test_chain)

        abet_map[char] = len(new_chain)
        print('Lowest for ' + char + ':', len(new_chain))

    sorted_abet_map = sorted(abet_map.items(), key=lambda item: item[1])
    lowest = sorted_abet_map[0][1]

    # print(lowest)
    return lowest


print('Calculating answers... NOTE: This can take a while')
print('Part 1:', part1(global_chain))
print('Part 2:', part2(global_chain))
