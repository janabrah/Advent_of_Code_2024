import numpy as np


def importFile(filename):
    f = open("./day_10/" + filename + ".txt")
    input = []
    for line in f:
        input.append([int(i) for i in line.strip("\n")])
    return input


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def partOne():
    myMap = importFile("input")
    total = 0
    for i in range(len(myMap)):
        for j in range(len(myMap)):
            if myMap[i][j] == 0:
                total += countPeaks(myMap, i, j)
    return total


def countPeaks(myMap, i, j):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    previousSet = set([(i, j)])
    for target in range(1, 10):
        currentSet = set()
        for source in previousSet:
            for dir in dirs:
                newI = source[0] + dir[0]
                newJ = source[1] + dir[1]
                if newI >= 0 and newI < len(myMap) and newJ >= 0 and newJ < len(myMap):
                    if myMap[newI][newJ] == target:
                        currentSet.add((newI, newJ))
        previousSet = currentSet
    return len(previousSet)


def partTwo():
    myMap = importFile("input")
    total = 0
    for i in range(len(myMap)):
        for j in range(len(myMap)):
            if myMap[i][j] == 0:
                total += countTrails(myMap, i, j)
    return total


def countTrails(myMap, i, j):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    previousTrails = [(i, j)]
    for target in range(1, 10):
        currentTrails = []
        for source in previousTrails:
            for dir in dirs:
                newI = source[0] + dir[0]
                newJ = source[1] + dir[1]
                if newI >= 0 and newI < len(myMap) and newJ >= 0 and newJ < len(myMap):
                    if myMap[newI][newJ] == target:
                        currentTrails.append((newI, newJ))
        previousTrails = currentTrails
    return len(previousTrails)


print(partTwo())
