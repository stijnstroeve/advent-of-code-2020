import math

lines = open("input.txt").read().split('\n')

ids = []

for line in lines:
    r_s = 0
    r_e = 127
    c_s = 0
    c_e = 7
    for char in line:
        if char == 'F':
            r_e = math.floor(r_e - (r_e - r_s) / 2)
        if char == 'B':
            r_s = math.ceil(r_s + (r_e - r_s) / 2)

        if char == 'L':
            c_e = math.floor(c_e - (c_e - c_s) / 2)
        if char == 'R':
            c_s = math.ceil(c_s + (c_e - c_s) / 2)

    if r_s != r_e or c_s != c_e:
        print('Error:', r_s, r_e)

    row = r_s
    column = c_s
    id = row * 8 + column

    ids.append(id)

ids = sorted(ids)

print('Highest id:', max(ids))

for i, id in enumerate(ids):
    p_id = ids[i-1]

    if p_id + 1 != id and p_id != ids[len(ids) - 1]:
        print('My seat:', p_id + 1)
        break
