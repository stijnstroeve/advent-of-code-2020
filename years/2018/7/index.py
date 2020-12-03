lines = open("input.txt").read().split('\n')


def get_individual_letters():
    x = [a[5] for a in lines]
    y = [a[36] for a in lines]

    return sorted(list(set(x + y)))


def get_starting_letter():
    start = [a[5] for a in lines]
    end = [a[36] for a in lines]

    return [x for x in start if x not in end][0]


def get_ending_letter():
    start = [a[5] for a in lines]
    end = [a[36] for a in lines]

    return [x for x in end if x not in start][0]

def get_letter_map():
    map = []
    start = [a[5] for a in lines]
    end = [a[36] for a in lines]

    for i, letter in enumerate(start):
        map.append((letter, end[i]))

    return map


def get_children(letter_map, letter):
    reqs = []

    for letter_t in letter_map:
        if(letter_t[0]) != letter:
            continue

        reqs.append(letter_t[1])

    return sorted(reqs)


def get_parents(letter_map, letter):
    nodes = []

    for letter_t in letter_map:
        if(letter_t[1]) == letter:
            nodes.append(letter_t[0])

    nodes = sorted(nodes)
    nodes.reverse()

    return nodes


i = 0
t = ''
unlocked = []
# def parse_letter_node(letter_map, node, end_letter):
#     global unlocked
#     global t
#     global i
#
#     children = get_children(letter_map, node)
#     unlocked = unlocked + children
#     unlocked = list(set(unlocked))
#     unlocked = sorted(unlocked)
#     print(str(i),unlocked)
#     i+=1
#
#     if len(unlocked) == 0:
#         return t
#
#     new_l = unlocked.pop(0)
#
#     t += new_l
#
#     # children = get_children(letter_map, node)
#     return parse_letter_node(letter_map, new_l, node)
#
#     # for node in unlocked:
#
#     # if len(children) > 0:
#     #     for child in children:
#     #         if child != end_letter:
#     #             unlocked.append(child)
#     #             # t += child
#     #             parse_letter_node(letter_map, child, end_letter)
#
#     # return
#
# def reverse_tree_search(letter_map, end_letter):
#     global unlocked
#
#     parents = get_parents(letter_map, end_letter)
#     unlocked = unlocked + parents
#     unlocked = list(set(unlocked))
#     unlocked = sorted(unlocked)
#     unlocked.reverse()
#
#     for node in unlocked:
#
#
#     print(unlocked)

visited_nodes = []


def has_requirements(letter_map, node):
    global visited_nodes
    parents = get_parents(letter_map, node)

    print('BLA', parents)

    for parent in parents:
        if parent not in visited_nodes:
            return False

    return True


def parse_letter_node(letter_map, node, end_letter, start_letter):
    global unlocked
    global visited_nodes
    global t
    global i

    if not has_requirements(letter_map, node):
        parents = get_parents(letter_map, node)
        print(str(i), node)

        return parse_letter_node(letter_map, parents[0], end_letter, start_letter)

    # print()

    children = get_children(letter_map, node)
    # children = [x for x in children if x not in visited_nodes]

    unlocked = unlocked + children
    unlocked = list(set(unlocked))
    unlocked = sorted(unlocked)
    print(str(i),unlocked, node)
    i+=1

    if len(unlocked) == 0:
        return t

    if node not in unlocked:
        new_l = unlocked.pop(0)
    else:
        new_l = node
        unlocked.remove(new_l)

    t += new_l
    visited_nodes.append(new_l)
    #
    # # children = get_children(letter_map, node)
    return parse_letter_node(letter_map, new_l, end_letter, start_letter)

    # for node in unlocked:
    # MENBAFOPHIJLQRSWXZ
    # if len(children) > 0:
    #     for child in children:
    #         if child != end_letter:
    #             unlocked.append(child)
    #             # t += child
    #             parse_letter_node(letter_map, child, end_letter)

    # return


letter_map = get_letter_map()
start_letter = get_starting_letter()
end_letter = get_ending_letter()
visited_nodes.append(start_letter)

# print(letter_map)
print(parse_letter_node(letter_map, start_letter, end_letter, start_letter))
# print(start_letter + t + end_letter)



