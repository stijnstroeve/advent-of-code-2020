
lines = [x.split('\n') for x in open("input.txt").read().split('\n\n')]


def part1():
    sum = 0
    for group in lines:
        answers = []
        for person in group:
            for answer in person:
                answers.append(answer)

        answers = list(set(answers))
        sum += len(answers)

    return sum


def part2():
    sum = 0
    for group in lines:
        answers = {}
        for person in group:
            for answer in person:
                if answer not in answers:
                    answers[answer] = 0

                answers[answer] += 1
        print(answers)
        for item in answers.items():
            answer = item[0]
            amount = item[1]

            if amount == len(group):
                sum += 1

            print(answer, amount)
        # answers = list(set(answers))
        # sum += len(answers)

    return sum


print('Part 1:', part1())
print('Part 2:', part2())