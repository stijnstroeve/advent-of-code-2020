import re
import json

lines = [x.replace('\n', ' ') for x in open("input.txt").read().split('\n\n')]

valid_t = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
v_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid = 0


def is_valid(key, value):
    if key == 'byr':
        return len(str(value)) == 4 and value.isdigit() and int(value) >= 1920 and int(value) <= 2002
    if key == 'iyr':
        return len(str(value)) == 4 and value.isdigit() and int(value) >= 2010 and int(value) <= 2020
    if key == 'eyr':
        return len(str(value)) == 4 and value.isdigit() and int(value) >= 2020 and int(value) <= 2030

    if key == 'hgt':
        if 'cm' not in value and 'in' not in value:
            return False

        type = value[-2:]
        amount = int(value[:len(value) - 2])

        if type == 'cm':
            return 150 <= amount <= 193

        if type == 'in':
            return 59 <= amount <= 76

        return False

    if key == 'hcl':
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)

        return match is not None

    if key == 'ecl':
        return value in v_ecl

    if key == 'pid':
        return len(str(value)) == 9 and int(value) > 0 and value.isdigit()

    if key == 'cid':
        return True

    return False

print(';e', len(lines))
i = 0
tfd = []
for line in lines:

    t = [x.split(':') for x in line.split(' ')]
    print(t)

    m = {}


    is_invalid = False
    for v in valid_t:
        if v not in line:
            is_invalid = True
            m['missing'] = True
            break


    for id in t:

        if id[0] not in valid_t and id[0] != 'cid':
            is_invalid = True


        m[id[0]] = is_valid(id[0], id[1])
        if not is_valid(id[0], id[1]):
            # print(id)
            is_invalid = True


    if is_invalid == False:
        valid += 1

    print(m)
    tfd.append(m)
    i += 1

output = open('output.json', 'w+')
output.write(json.dumps(tfd, indent=4))

part1 = valid
print("Part 1: ", part1)