import numpy as np
import time


def loadInput(filename):
    myInput = []
    f = open("./day_14/" + filename + ".txt")
    for line in f:
        row = line.strip("\n").split(" v")
        start = row[0].split("=")[1].split(",")
        end = row[1].split("=")[1].split(",")
        myInput.append((((int(start[0]), int(start[1])), (int(end[0]), int(end[1])))))
    return myInput


def prettyPrint(robots, mapSize):
    myMap = [[0 for i in range(mapSize[0])] for j in range(mapSize[1])]
    for robot in robots:
        myMap[robot[0][1]][robot[0][0]] += 1
    for i in range(len(myMap)):
        for j in range(len(myMap[i])):
            if myMap[i][j] == 0:
                myMap[i][j] = " "
            else:
                myMap[i][j] = str(myMap[i][j])
    for row in myMap:
        print("".join(row))
    print()


def partOne():
    fileType = "input"
    mapSize = (11, 7)
    if fileType == "input":
        mapSize = (101, 103)
    steps = 100
    robots = loadInput(fileType)
    print(robots)
    finalLocs = []
    for robot in robots:
        finalLocs.append(runRobot(robot[0], robot[1], mapSize, steps))
    print(finalLocs)
    quads = countQuadrants(finalLocs, mapSize)
    print(quads)
    return quads[0] * quads[1] * quads[2] * quads[3]


def partOneMin():
    fileType = "input"
    mapSize = (11, 7)
    if fileType == "input":
        mapSize = (101, 103)
    steps = 10000
    minDanger = np.infin
    robots = loadInput(fileType)
    print(robots)
    finalLocs = []
    for robot in robots:
        finalLocs.append(runRobot(robot[0], robot[1], mapSize, steps))
    print(finalLocs)
    quads = countQuadrants(finalLocs, mapSize)
    print(quads)
    return quads[0] * quads[1] * quads[2] * quads[3]


def countQuadrants(locations, mapSize):
    newMapSize = (mapSize[0] - 1, mapSize[1] - 1)
    quads = [0, 0, 0, 0]
    for location in locations:
        if location[0] < newMapSize[0] / 2 and location[1] < newMapSize[1] / 2:
            quads[0] += 1
        elif location[0] < newMapSize[0] / 2 and location[1] > newMapSize[1] / 2:
            quads[1] += 1
        elif location[0] > newMapSize[0] / 2 and location[1] < newMapSize[1] / 2:
            quads[2] += 1
        elif location[0] > newMapSize[0] / 2 and location[1] > newMapSize[1] / 2:
            quads[3] += 1
    return quads


def stepRobot(location, velocity, mapSize):
    return (
        (location[0] + velocity[0]) % mapSize[0],
        (location[1] + velocity[1]) % mapSize[1],
    )


def runRobot(startLoc, velocity, mapSize, steps):
    for i in range(steps):
        startLoc = stepRobot(startLoc, velocity, mapSize)
    return startLoc


def partTwo():
    fileType = "input"
    mapSize = (11, 7)
    if fileType == "input":
        mapSize = (101, 103)
    steps = 100
    robots = loadInput(fileType)
    finalLocs = []
    for step in range(10000):
        for i in range(len(robots)):
            robots[i] = (stepRobot(robots[i][0], robots[i][1], mapSize), robots[i][1])
        if step % 101 == 65:  # treeIsh(robots):
            print(step)
            prettyPrint(robots, mapSize)
            time.sleep(1)
    quads = countQuadrants(finalLocs, mapSize)
    return quads[0] * quads[1] * quads[2] * quads[3]


def treeIsh(robots):
    treeVibe = 0
    for robot in robots:
        if robot[0][0] == 15:
            treeVibe += 1
    if treeVibe > len(robots) / 30:
        return True
    return False


# print(partOne())
print(partTwo())
