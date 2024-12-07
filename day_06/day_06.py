import numpy as np
import time
import copy


def getFile(name):
    f = open("./day_06/" + name + ".txt")
    input = []
    for line in f:
        input.append([i for i in line.strip("\n")])
    return input[:130]


dirKey = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}
combos = {
    (0, 0, 0, 0): ".",
    (1, 0, 0, 0): "^",
    (0, 1, 0, 0): ">",
    (0, 0, 1, 0): "v",
    (0, 0, 0, 1): "<",
    (1, 1, 0, 0): "a",
    (1, 0, 1, 0): "b",
    (1, 0, 0, 1): "c",
    (0, 1, 1, 0): "d",
    (0, 1, 0, 1): "e",
    (0, 0, 1, 1): "f",
    (1, 1, 1, 0): "g",
    (1, 1, 0, 1): "h",
    (1, 0, 1, 1): "i",
    (0, 1, 1, 1): "j",
    (1, 1, 1, 1): "k",
}
reverseDirs = {
    "^": (1, 0, 0, 0),
    ">": (0, 1, 0, 0),
    "v": (0, 0, 1, 0),
    "<": (0, 0, 0, 1),
    "a": (1, 1, 0, 0),
    "b": (1, 0, 1, 0),
    "c": (1, 0, 0, 1),
    "d": (0, 1, 1, 0),
    "e": (0, 1, 0, 1),
    "f": (0, 0, 1, 1),
    "g": (1, 1, 1, 0),
    "h": (1, 1, 0, 1),
    "i": (1, 0, 1, 1),
    "j": (0, 1, 1, 1),
    "k": (1, 1, 1, 1),
}


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def findStart(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "^":
                return (i, j)


def step(map, location, dir, distance):
    if (
        location[0] + dir[0] < 0
        or location[0] + dir[0] >= len(map)
        or location[1] + dir[1] < 0
        or location[1] + dir[1] >= len(map[0])
    ):
        return ((location[0], location[1]), dir, distance, True)
    if map[location[0] + dir[0]][location[1] + dir[1]] == ".":
        map[location[0] + dir[0]][location[1] + dir[1]] = dirKey[dir]
        return ((location[0] + dir[0], location[1] + dir[1]), dir, distance + 1, False)
    elif map[location[0] + dir[0]][location[1] + dir[1]] != "#":
        oldVal = map[location[0] + dir[0]][location[1] + dir[1]]
        currentVal = dirKey[dir]
        newVal = combos[
            tuple(
                [reverseDirs[oldVal][i] + reverseDirs[currentVal][i] for i in range(4)]
            )
        ]
        map[location[0] + dir[0]][location[1] + dir[1]] = newVal
        return ((location[0] + dir[0], location[1] + dir[1]), dir, distance, False)
    else:
        newDir = rotateDir(dir)
        return ((location[0], location[1]), newDir, distance, False)


def rotateDir(dir):
    return (dir[1], -dir[0])


def partOne(filename):
    input = getFile(filename)
    location = findStart(input)
    dir = (-1, 0)
    distance = 1
    while True:
        location, dir, distance, done = step(input, location, dir, distance)
        if done:
            prettyPrint(input)
            return distance


def partTwoInternal(myMap, filename, blockage):
    # myMap = getFile(filename)
    location = findStart(myMap)
    myMap[blockage[0]][blockage[1]] = "#"
    try:
        dir = (-1, 0)
        distance = 1
        while True:
            location, dir, distance, done = step(myMap, location, dir, distance)
            if done:
                return 0
    except:
        # print(blockage)
        return 1


def basicCopy(inputMap):
    newMap = []
    for i in range(len(inputMap)):
        newMap.append([j for j in inputMap[i]])
    return newMap


def partTwoBad(filename):
    blocks = []
    baseMap = getFile(filename)
    myMap = basicCopy(baseMap)
    location = findStart(myMap)
    dir = (-1, 0)
    distance = 1
    spots = 0
    while True:
        location, dir, distance, done = step(myMap, location, dir, distance)
        if not location in blocks:
            test = partTwoInternal(basicCopy(baseMap), filename, location)
            if test == 1:
                blocks.append(location)
                spots += 1
        if done:
            return spots


def partTwoGood():
    location = findStart(input)
    input[location[0]][location[1]] = "v"
    dir = (1, 0)
    distance = 1
    while True:
        prettyPrint(input)
        location, dir, distance, done = step(
            input,
            location,
            dir,
            distance,
        )
        if done:
            break
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != "." and input[i][j] != "#":
                key = reverseDirs[input[i][j]]
                input[i][j] = combos[(key[2], key[3], key[0], key[1])]
    prettyPrint(input)
    return
    while True:
        location, dir, distance, done = step(input, location, dir, distance)
        if (
            input[location[0] + dir[0]][location[1] + dir[1]] != "."
            and input[location[0] + dir[0]][location[1] + dir[1]] != "#"
        ):
            print(dirKey[dir], input[location[0] + dir[0]][location[1] + dir[1]])
        if done:
            prettyPrint(input)
            return distance


starttime = time.time()
print(partTwoBad("input"))
print(time.time() - starttime)
