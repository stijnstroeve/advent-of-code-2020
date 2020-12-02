import math
coords = [tuple([int(z) for z in x.split(', ')]) for x in open("input.txt").read().split('\n')]
coords_map = {}


def get_coords(entry):
    return tuple([int(x) for x in entry[0].split(',')])


def distance_to_closest(x, y):
    global coords_map

    closest = math.inf
    closest_ids = []

    for entry in coords_map.items():
        coords = get_coords(entry)
        tX = coords[0]
        tY = coords[1]

        dX = x - tX
        dY = y - tY

        distance = abs(dX) + abs(dY)

        if distance < closest:
            closest = distance

            closest_ids = []

        if distance == closest:
            closest_ids.append(entry[1])

    return closest_ids, closest


def print_map():
    w = get_borders()[0]
    h = get_borders()[1]

    for y in range(h):
        fs = ''
        for x in range(w):

            closest = distance_to_closest(x, y)
            if len(closest[0]) > 1:
                fs += '.'

            else:
                if closest[1] == 0:
                    fs += closest[0][0].upper()
                else:
                    fs += closest[0][0]

        print(fs)


def get_borders():
    w = max([int(x[0].split(',')[0]) for x in coords_map.items()]) + 1
    h = max([int(x[0].split(',')[1]) for x in coords_map.items()]) + 1

    return w, h


def get_border_ids():
    borders = get_borders()

    ids = []

    for y in range(borders[1]):
        closest = distance_to_closest(0, y)[0]
        if len(closest) == 1:
            ids = ids + closest
    for y in range(borders[1]):
        closest = distance_to_closest(borders[0], y)[0]
        if len(closest) == 1:
            ids = ids + closest

    for x in range(borders[1]):
        closest = distance_to_closest(x, 0)[0]
        if len(closest) == 1:
            ids = ids + closest
    for x in range(borders[1]):
        closest = distance_to_closest(x, borders[1])[0]
        if len(closest) == 1:
            ids = ids + closest

    ids = list(set(ids))

    return ids


def prepare_map(coords):
    all_ids = []
    # abet = 'abcdefghijklmnopqrstuvwxyz'
    id = 0
    for coord in coords:
        pcoord = str(coord[0]) + ',' + str(coord[1])

        coords_map[pcoord] = id
        all_ids.append(id)
        id += 1

    return all_ids


def calculate_map(ids):
    area_sizes = {}

    w = get_borders()[0]
    h = get_borders()[1]

    for y in range(h):
        for x in range(w):

            closest = distance_to_closest(x, y)
            if len(closest[0]) == 1 and closest[0][0] in ids:
                if closest[0][0] not in area_sizes:
                    area_sizes[closest[0][0]] = 0

                area_sizes[closest[0][0]] += 1

    return area_sizes


def part1():
    ids = prepare_map(coords)

    ids_left = [x for x in ids if x not in get_border_ids()]

    final_map = calculate_map(ids_left)
    final_map = sorted(final_map.items(), key=lambda item: item[1])
    final_map.reverse()

    return final_map[0][1]



print('Part 1:', part1())

