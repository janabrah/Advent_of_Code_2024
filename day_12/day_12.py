import numpy as np


def loadInput():
    myInput = []
    f = open("./day_12/input.txt")
    for line in f:
        myInput.append(list(line.strip("\n")))
    return myInput


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def partOne():
    myInput = loadInput()
    prettyPrint(myInput)
    tot = 0
    for i in range(len(myInput)):
        for j in range(len(myInput[i])):
            if myInput[i][j] != ".":
                (area, walls) = removePlot(myInput, i, j, myInput[i][j])
                tot += area * len(walls)
    return tot


def removePlot(myInput, i, j, letter):
    walls = []
    if (
        i < 0
        or i >= len(myInput)
        or j < 0
        or j >= len(myInput[i])
        or myInput[i][j] == "."
        or myInput[i][j] != letter
    ):
        return 0, walls
    walls.append((i - 0.5, j))
    walls.append((i + 0.5, j))
    walls.append((i, j - 0.5))
    walls.append((i, j + 0.5))
    workingLetter = myInput[i][j]
    myInput[i][j] = "."
    area = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dir in dirs:
        newArea, newWalls = removePlot(myInput, i + dir[0], j + dir[1], letter)
        area += newArea
        for newWall in newWalls:
            if newWall in walls:
                walls.remove(newWall)
            else:
                walls.append(newWall)
    return (area, walls)


def removePlotTwo(myInput, i, j, letter):
    walls = []
    if (
        i < 0
        or i >= len(myInput)
        or j < 0
        or j >= len(myInput[i])
        or myInput[i][j] == "."
        or myInput[i][j] != letter
    ):
        return 0, walls
    walls.append(((i - 0.5, j - 0.5), (i + 0.5, j - 0.5), -1))
    walls.append(((i - 0.5, j + 0.5), (i + 0.5, j + 0.5), 1))
    walls.append(((i - 0.5, j - 0.5), (i - 0.5, j + 0.5), -1))
    walls.append(((i + 0.5, j - 0.5), (i + 0.5, j + 0.5), 1))
    workingLetter = myInput[i][j]
    myInput[i][j] = "."
    area = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dir in dirs:
        newArea, newWalls = removePlotTwo(myInput, i + dir[0], j + dir[1], letter)
        area += newArea
        for newWall in newWalls:
            tempWall = (newWall[0], newWall[1], -newWall[2])
            if tempWall in walls:
                walls.remove(tempWall)
            else:
                walls.append(newWall)
    return (area, walls)


def collapseWalls(walls):
    for i in range(len(walls)):
        for j in range(len(walls))[i + 1 :]:
            if j < len(walls):
                jfirst = walls[i][0] == walls[j][1]
                ifirst = walls[j][0] == walls[i][1]
                if ifirst or jfirst:
                    ymatch = (
                        walls[i][0][0] == walls[i][1][0]
                        and walls[i][0][0] == walls[j][0][0]
                        and walls[i][0][0] == walls[j][1][0]
                    )
                    xmatch = (
                        walls[i][0][1] == walls[i][1][1]
                        and walls[i][0][1] == walls[j][0][1]
                        and walls[i][0][1] == walls[j][1][1]
                    )
                    sideMatch = walls[i][2] == walls[j][2]
                    if (ymatch or xmatch) and sideMatch:
                        jpop = walls.pop(j)
                        ipop = walls.pop(i)
                        if ifirst:
                            walls.append((ipop[0], jpop[1], jpop[2]))
                        else:
                            walls.append((jpop[0], ipop[1], jpop[2]))
    return walls


def collapseAllWalls(walls):
    wallLen = len(walls)
    while True:
        walls = collapseWalls(walls)
        if len(walls) == wallLen:
            return walls
        wallLen = len(walls)


def partTwo():
    myInput = loadInput()
    tot = 0
    prettyPrint(myInput)
    for i in range(len(myInput)):
        for j in range(len(myInput[i])):
            if myInput[i][j] != ".":
                (area, walls) = removePlotTwo(myInput, i, j, myInput[i][j])
                walls = collapseAllWalls(walls)
                tot += area * len(walls)
                # prettyPrint(myInput)
                print(area * len(walls), area, len(walls))
    return tot


# print(partOne())
# print(partOne() == 1930)
print(partTwo())
