import numpy as np


def loadInput():
    myInput = []
    f = open("./day_xx/input.txt")
    for line in f:
        myInput.append([int(i) for i in line.strip("\n").split()])
    return myInput


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def partOne():
    return


def partTwo():
    return


print(partOne())
print(partTwo())
