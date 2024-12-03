import numpy as np


def partOne():
    data = ""
    f = open("./day_03/input.txt")
    for line in f:
        data += line
    muls = findMuls(data)
    total = 0
    for mul in muls:
        total += mul[0] * mul[1]
    print("Part one is: " + str(total))


def partTwo():
    data = ""
    f = open("./day_03/input.txt")
    for line in f:
        data += line
    muls = findMuls(data, enableable=True)
    total = 0
    for mul in muls:
        total += mul[0] * mul[1]
    print("Part two is: " + str(total))


def findMuls(data, enableable=False):
    i = 0
    inmul = False
    current = ""
    potentials = []
    enabled = True
    while i < len(data):
        if enabled:
            if data[i : i + 7] == "don't()":
                enabled = False or not enableable
                i += 7
            if data[i : i + 4] == "mul(":
                current = ""
                i += 4
                inmul = True
            else:
                if inmul:
                    if data[i] == ")":
                        inmul = False
                        potentials.append(current)
                        current = ""
                    current += data[i]
                i += 1
        else:
            if data[i : i + 4] == "do()":
                enabled = True
                i += 4
            else:
                i += 1
    reals = []
    for potential in potentials:
        pair = potential.split(",")
        if len(pair) == 2 and pair[0].isdigit() and pair[1].isdigit():
            reals.append([int(pair[0]), int(pair[1])])
    return reals


partOne()
partTwo()
