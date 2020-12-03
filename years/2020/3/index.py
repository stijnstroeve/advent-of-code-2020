# lines = [int(item) for item in open("input.txt").read().split('\n')]
lines = open("input.txt").read().split('\n')

# print(lines)

map = [x for x in lines]

def is_tree(x_t, y_t):
    if x_t > len(map[0]) - 1 or y_t > len(map) - 1: return False
    # print(y)
    return map[y_t][x_t] == '#'



def add_map():
    global map

    for i, line in enumerate(map):
        map[i] = line + line


x = 0
y = 0
def run(slope_x, slope_y):
    global x
    global y
    global map

    encountered_trees = []
    map = lines

    x = 0
    y = 0

    def do_run():
        global x
        global y

        x += slope_x
        y += slope_y

        if x > len(map[0]):
            add_map()

        if is_tree(x, y):
            encountered_trees.append((x, y))


    while (y < len(map)):
        do_run()

    return len(encountered_trees)

# print(map)

# print(encountered_trees)
# print(run(3, 1))
# print(run(2, 1))

# product =  * run(3, 1) * run(5, 1) * run(7, 1) * run(1, 2)
coords_to_check = [(1,1), (3,1), (5,1), (7,1), (1,2)]

m = 1

for to_check in coords_to_check:
    m *= run(to_check[0], to_check[1])

print(run(1,1), y)
print(run(3,1), y)
print(run(5,1), y)
print(run(7,1), y)
print(run(1,2), y)
print(m)
# print(product)