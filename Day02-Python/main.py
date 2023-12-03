limits = {"red": 12, "green": 13, "blue": 14}


def part1():
    sum = 0
    f = open("input.txt", "r")
    for line in f.readlines():
        exceeds = False
        game, sets = line.split(":")
        for subset in sets.split(";"):
            for group in subset.split(", "):
                value = int(group.strip().split(" ")[0])
                limit = limits[group.strip().split(" ")[1]]
                # print("Game {} with  colorgroup {} has value {} and limit {}. Exceeds = {}".format(game,group, value, limit, value > limit))
                if value > limit:
                    exceeds = True
                    break
            if exceeds:
                break
        if not exceeds:
            sum += int(game[5:])
    return sum


def prod(arr):
    prod = 1
    for x in arr:
        prod *= x
    return prod


def part2():
    sum = 0
    f = open("input.txt", "r")
    for line in f.readlines():
        game, sets = line.split(":")
        subsetmins = {"red": 0, "green": 0, "blue": 0}
        for subset in [x.strip() for x in sets.split(";")]:
            for group in [x.strip() for x in subset.split(",")]:
                value, color = group.strip().split(" ")
                if int(value) > subsetmins[color]:
                    subsetmins[color] = int(value)
        values = subsetmins.values()
        power = prod(values)
        sum += power
    return sum


print(part1())
print(part2())
