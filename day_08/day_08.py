import numpy as np

f = open("./day_08/input.txt")
input = []
for line in f:
    input.append(list(line.strip("\n")))


def prettyPrint(myArray):
    printStr = ""
    for i in range(len(myArray)):
        for j in range(len(myArray[i])):
            if myArray[i][j] == True:
                printStr += "#"
            elif myArray[i][j] == False:
                printStr += "."
            else:
                printStr += myArray[i][j]
        printStr += "\n"
    print(printStr)


def partOne():
    prettyPrint(input)
    nodeMap = [[False for i in range(len(input[0]))] for j in range(len(input))]
    found = {}
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != ".":
                if input[i][j] in found:
                    for node in found[input[i][j]]:
                        vect = (node[0] - i, node[1] - j)
                        if (
                            i - vect[0] >= 0
                            and i - vect[0] < len(nodeMap)
                            and j - vect[1] >= 0
                            and j - vect[1] < len(nodeMap[0])
                        ):
                            nodeMap[i - vect[0]][j - vect[1]] = True
                        if (
                            i + 2 * vect[0] >= 0
                            and i + 2 * vect[0] < len(nodeMap)
                            and j + 2 * vect[1] >= 0
                            and j + 2 * vect[1] < len(nodeMap[0])
                        ):
                            nodeMap[i + 2 * vect[0]][j + 2 * vect[1]] = True
                    found[input[i][j]].append((i, j))
                else:
                    found[input[i][j]] = [(i, j)]
    total = 0
    for i in range(len(nodeMap)):
        for j in range(len(nodeMap[i])):
            if nodeMap[i][j]:
                total += 1
    return total


def partTwo():
    prettyPrint(input)
    nodeMap = [[False for i in range(len(input[0]))] for j in range(len(input))]
    found = {}
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != ".":
                if input[i][j] in found:
                    for node in found[input[i][j]]:
                        vect = (node[0] - i, node[1] - j)
                        divisor = np.gcd(vect[0], vect[1])
                        vect = (int(vect[0] / divisor), int(vect[1] / divisor))
                        myIter = getIterator(
                            (i, j), vect, (len(nodeMap), len(nodeMap[0]))
                        )
                        print((i, j), node, vect, myIter)
                        for mul in myIter:
                            if (
                                i + mul * vect[0] >= 0
                                and i + mul * vect[0] < len(nodeMap)
                                and j + mul * vect[1] >= 0
                                and j + mul * vect[1] < len(nodeMap[0])
                            ):
                                nodeMap[i + mul * vect[0]][j + mul * vect[1]] = True
                    found[input[i][j]].append((i, j))
                else:
                    found[input[i][j]] = [(i, j)]
    total = 0
    for i in range(len(nodeMap)):
        for j in range(len(nodeMap[i])):
            if nodeMap[i][j]:
                total += 1
    prettyPrint(nodeMap)
    return total


def getIterator(startPoint, vect, dims):
    if vect[0] == 0:
        return getIterator(
            (startPoint[1], startPoint[0]), (vect[1], vect[0]), (dims[1], dims[0])
        )
    if vect[0] < 0:
        return [
            -1 * i
            for i in getIterator(
                (startPoint[0], startPoint[1]), (vect[0] * -1, vect[1] * -1), dims
            )
        ]
    left = int(startPoint[0] / vect[0] + 2)
    right = int((dims[0] - startPoint[0]) / vect[0] + 2)
    return list(range(-left, right))


print(partTwo())
# print(getIterator((3, 7), (2, 5), (12, 14)))
