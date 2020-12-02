from collections import Counter

lines = open("input.txt").read().split('\n')


def part1():
    coords_map = []

    for line in lines:

        split = line.split(' ')

        xOffset = int(split[2].replace(':', '').split(',')[0])
        yOffset = int(split[2].replace(':', '').split(',')[1])

        width = int(split[3].split('x')[0])
        height = int(split[3].split('x')[1])

        for x in range(width):
            for y in range(height):
                coord_string = str(x + xOffset) + ',' + str(y + yOffset)
                coords_map.append(coord_string)

    # Calculate the duplicate items
    doubles = [k for k, v in Counter(coords_map).items() if v > 1]

    return len(doubles)


def part2():
    coords_map = []

    ids = []
    coords_dict = {}

    for line in lines:

        split = line.split(' ')
        ids.append(split[0])

        xOffset = int(split[2].replace(':', '').split(',')[0])
        yOffset = int(split[2].replace(':', '').split(',')[1])

        width = int(split[3].split('x')[0])
        height = int(split[3].split('x')[1])


        for x in range(width):
            for y in range(height):
                coord_string = str(x + xOffset) + ',' + str(y + yOffset)
                coords_map.append(coord_string)

                if coord_string in coords_dict:
                    coords_dict[coord_string].append(split[0])
                else:
                    coords_dict[coord_string] = [split[0]]


    # Calculate the duplicate items
    doubles = [k for k, v in Counter(coords_map).items() if v > 1]

    overlapping = []

    # I know this is a quite inefficient, but its the best I could do in the shortest time possible.
    for double in doubles:
        id_d = coords_dict[double]

        for o in id_d:
            overlapping.append(o)

    overlapping_ids = list(set(overlapping))

    for o_id in overlapping_ids:
        ids.remove(o_id)


    # Because only 1 item cannot overlap we pick the first item.
    return ids[0]


print('Part 1:', part1())
print('Part 2:', part2())
