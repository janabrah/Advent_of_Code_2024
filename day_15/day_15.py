import numpy as np


def loadInput(filename):
    myMap = []
    instructions = []
    f = open("./day_15/" + filename + ".txt")
    chunk = []
    doingMap = True
    for line in f:
        if line == "\n":
            doingMap = False
            continue
        if doingMap:
            myMap.append([i for i in line.strip("\n")])
        else:
            for char in line.strip("\n"):
                instructions.append(char)
    return (myMap, instructions)


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def doInstruction(myMap, myLoc, instruction):
    dir = (0, 0)
    if instruction == "<":
        dir = (0, -1)
    elif instruction == ">":
        dir = (0, 1)
    elif instruction == "^":
        dir = (-1, 0)
    elif instruction == "v":
        dir = (1, 0)
    else:
        return -1
    if myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] == ".":
        myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] = "@"
        myMap[myLoc[0]][myLoc[1]] = "."
        return ((myLoc[0] + dir[0], myLoc[1] + dir[1]), myMap)
    elif myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] == "#":
        return (myLoc, myMap)
    else:
        trying = True
        multiple = 2
        while trying:
            if myMap[myLoc[0] + multiple * dir[0]][myLoc[1] + multiple * dir[1]] == "#":
                trying = False
                return (myLoc, myMap)
            elif (
                myMap[myLoc[0] + multiple * dir[0]][myLoc[1] + multiple * dir[1]] == "."
            ):
                myMap[myLoc[0] + multiple * dir[0]][myLoc[1] + multiple * dir[1]] = "O"
                myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] = "@"
                myMap[myLoc[0]][myLoc[1]] = "."
                return ((myLoc[0] + dir[0], myLoc[1] + dir[1]), myMap)
            else:
                multiple += 1
    return (myLoc, myMap)


def partOne():
    myInput = loadInput("input")
    myMap = myInput[0]
    myLoc = (4, 4)
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if myMap[i][j] == "@":
                myLoc = (i, j)
    instructions = myInput[1]
    for instruction in instructions:
        myLoc, myMap = doInstruction(myMap, myLoc, instruction)
    prettyPrint(myInput[0])
    return getBoxLocations(myMap)


def getBoxLocations(myMap):
    total = 0
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if myMap[i][j] == "O" or myMap[i][j] == "[":
                total += 100 * i + j
    return total


def expandMap(myMap):
    newMap = []
    for i in range(len(myMap)):
        row = []
        for j in range(len(myMap[i])):
            if myMap[i][j] == "#":
                row.append("#")
                row.append("#")
            elif myMap[i][j] == ".":
                row.append(".")
                row.append(".")
            elif myMap[i][j] == "O":
                row.append("[")
                row.append("]")
            elif myMap[i][j] == "@":
                row.append("@")
                row.append(".")
        newMap.append(row)
    return newMap


def partTwo():
    myInput = loadInput("input")
    myMap = myInput[0]
    myMap = expandMap(myMap)
    prettyPrint(myMap)
    myLoc = (4, 4)
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if myMap[i][j] == "@":
                myLoc = (i, j)
    instructions = myInput[1]
    for instruction in instructions:
        myLoc, myMap = doInstructionTwo(myMap, myLoc, instruction)
    prettyPrint(myMap)
    return getBoxLocations(myMap)


def doInstructionTwo(myMap, myLoc, instruction):
    dir = (0, 0)
    if instruction == "<":
        dir = (0, -1)
    elif instruction == ">":
        dir = (0, 1)
    elif instruction == "^":
        dir = (-1, 0)
    elif instruction == "v":
        dir = (1, 0)
    else:
        return -1
    if myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] == ".":
        myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] = "@"
        myMap[myLoc[0]][myLoc[1]] = "."
        return ((myLoc[0] + dir[0], myLoc[1] + dir[1]), myMap)
    elif myMap[myLoc[0] + dir[0]][myLoc[1] + dir[1]] == "#":
        return (myLoc, myMap)
    else:
        if instruction == "<" or instruction == ">":
            return doInstructionTwoHor(myMap, myLoc, instruction)
        else:
            return doInstructionTwoVer(myMap, myLoc, instruction)


def doInstructionTwoHor(myMap, myLoc, instruction):
    dir = (0, 0)
    if instruction == "<":
        dir = (0, -1)
    elif instruction == ">":
        dir = (0, 1)
    else:
        return -1
    trying = True
    multiple = 2
    while trying:
        if myMap[myLoc[0] + multiple * dir[0]][myLoc[1] + multiple * dir[1]] == "#":
            trying = False
            return (myLoc, myMap)
        elif myMap[myLoc[0] + multiple * dir[0]][myLoc[1] + multiple * dir[1]] == ".":
            trying = False
        else:
            multiple += 1
    for i in range(multiple)[::-1]:
        myMap[myLoc[0]][myLoc[1] + (i + 1) * dir[1]] = myMap[myLoc[0]][
            myLoc[1] + i * dir[1]
        ]
        myMap[myLoc[0]][myLoc[1] + i * dir[1]] = "."
    return ((myLoc[0] + dir[0], myLoc[1] + dir[1]), myMap)


def doInstructionTwoVer(myMap, myLoc, instruction):
    dir = (1, 0)
    if instruction == "^":
        dir = (-1, 0)
    trying = True
    multiple = 1
    concerns = []
    newConcerns = [(myLoc[0] + dir[0], myLoc[1])]
    if myMap[myLoc[0] + multiple * dir[0]][myLoc[1] + multiple * dir[1]] == "[":
        newConcerns.append((myLoc[0] + dir[0], myLoc[1] + 1))
    else:
        newConcerns.append((myLoc[0] + dir[0], myLoc[1] - 1))
    while trying:
        trying = False
        temp = []
        for concern in newConcerns:
            concerns.append(concern)
            checking = (concern[0] + dir[0], concern[1])
            if myMap[concern[0] + dir[0]][concern[1]] == "#":
                return (myLoc, myMap)
            elif myMap[checking[0]][checking[1]] != ".":
                trying = True
                if not checking in temp:
                    temp.append(checking)
                if myMap[checking[0]][checking[1]] == "[":
                    if not (checking[0], checking[1] + 1) in temp:
                        temp.append((checking[0], checking[1] + 1))
                else:
                    if not (checking[0], checking[1] - 1) in temp:
                        temp.append((checking[0], checking[1] - 1))
        newConcerns = temp
    for concern in concerns[::-1]:
        myMap[concern[0] + dir[0]][concern[1]] = myMap[concern[0]][concern[1]]
        myMap[concern[0]][concern[1]] = "."
    myMap[myLoc[0]][myLoc[1]] = "."
    myMap[myLoc[0] + dir[0]][myLoc[1]] = "@"
    return ((myLoc[0] + dir[0], myLoc[1]), myMap)


# print(partOne())
print(partTwo())
