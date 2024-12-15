import numpy as np


def loadInput():
    myInput = []
    f = open("./day_13/input.txt")
    chunk = []
    for line in f:
        if "Button" in line:
            row = line.split(": ")[1].split(", ")
            chunk.append((int(row[0].split("+")[1]), int(row[1].split("+")[1])))
        elif "Prize" in line:
            row = line.split(": ")[1].split(", ")
            chunk.append((int(row[0].split("=")[1]), int(row[1].split("=")[1])))
        else:
            myInput.append(chunk)
            chunk = []
    myInput.append(chunk)
    return myInput


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def partOne():
    myInput = loadInput()
    total = 0
    for prizeData in myInput:
        if getPrize(prizeData) != getPrizeTwo(prizeData):
            print("lookatme")
        total += getPrizeTwo(prizeData)
    return total


def getPrize(prizeData):
    for i in range(101):
        x = prizeData[2][0] - i * prizeData[0][0]
        y = prizeData[2][1] - i * prizeData[0][1]
        if x % prizeData[1][0] == 0 and y / prizeData[1][1] == x / prizeData[1][0]:
            return 3 * i + x / prizeData[1][0]
    return 0


def getPrizeTwo(prizeData):
    if (
        prizeData[2][0] % prizeData[1][0] == 0
        and prizeData[2][1] / prizeData[1][1] == prizeData[2][0] / prizeData[1][0]
    ):
        return prizeData[2][0] % prizeData[0][0]
    a = np.array(
        [[prizeData[0][0], prizeData[1][0]], [prizeData[0][1], prizeData[1][1]]]
    )
    b = np.array([prizeData[2][0], prizeData[2][1]])
    x = np.linalg.solve(a, b)
    if (x[0] % 1 < 10**-4 or (1 - x[0]) % 1 < 10**-4) and (
        x[1] % 1 < 10**-4 or (1 - x[1]) % 1 < 10**-4
    ):
        return 3 * x[0] + x[1]
    return 0


def partTwo():
    myInput = loadInput()
    total = 0
    for prizeData in myInput:
        prizeData[2] = (
            prizeData[2][0] + 10000000000000,
            prizeData[2][1] + 10000000000000,
        )
        total += getPrizeTwo(prizeData)
    return total


print(partOne())
print(partTwo())
