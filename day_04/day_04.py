import numpy as np

f = open("./day_04/input.txt")
input = []
for line in f:
    input.append([".", ".", "."] + [i for i in line.strip("\n")] + [".", ".", "."])

for i in range(3):
    input = [["." for i in input[0]]] + input + [["." for i in input[0]]]


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def partOne():
    count = 0
    for i in range(len(input))[3:-3]:
        for j in range(len(input[i]))[3:-3]:
            if input[i][j] == "X":
                count += checkRight(input, i, j)
                count += checkDown(input, i, j)
                count += checkUpRight(input, i, j)
                count += checkDownRight(input, i, j)
                count += checkLeft(input, i, j)
                count += checkDownLeft(input, i, j)
                count += checkUpLeft(input, i, j)
                count += checkUp(input, i, j)
    return count


def checkRight(input, i, j):
    if input[i][j : j + 4] == ["X", "M", "A", "S"]:
        return 1
    return 0


def checkDown(input, i, j):
    if [input[i][j], input[i + 1][j], input[i + 2][j], input[i + 3][j]] == [
        "X",
        "M",
        "A",
        "S",
    ]:
        return 1
    return 0


def checkUpRight(input, i, j):
    if [input[i][j], input[i - 1][j + 1], input[i - 2][j + 2], input[i - 3][j + 3]] == [
        "X",
        "M",
        "A",
        "S",
    ]:
        return 1
    return 0


def checkDownRight(input, i, j):
    if [input[i][j], input[i + 1][j + 1], input[i + 2][j + 2], input[i + 3][j + 3]] == [
        "X",
        "M",
        "A",
        "S",
    ]:
        return 1
    return 0


def checkLeft(input, i, j):
    if input[i][j - 3 : j + 1] == ["S", "A", "M", "X"]:
        return 1
    return 0


def checkDownLeft(input, i, j):
    if [input[i][j], input[i + 1][j - 1], input[i + 2][j - 2], input[i + 3][j - 3]] == [
        "X",
        "M",
        "A",
        "S",
    ]:
        return 1
    return 0


def checkUpLeft(input, i, j):
    if [input[i][j], input[i - 1][j - 1], input[i - 2][j - 2], input[i - 3][j - 3]] == [
        "X",
        "M",
        "A",
        "S",
    ]:
        return 1
    return 0


def checkUp(input, i, j):
    if [input[i][j], input[i - 1][j], input[i - 2][j], input[i - 3][j]] == [
        "X",
        "M",
        "A",
        "S",
    ]:
        return 1
    return 0


def partTwo():
    count = 0
    for i in range(len(input))[4:-4]:
        for j in range(len(input[i]))[4:-4]:
            if input[i][j] == "A":
                count += checkRightward(input, i, j)
                count += checkDownward(input, i, j)
                count += checkUpward(input, i, j)
                count += checkLeftward(input, i, j)
    return count


def checkRightward(input, i, j):
    if (
        input[i - 1][j - 1] == "M"
        and input[i - 1][j + 1] == "S"
        and input[i + 1][j - 1] == "M"
        and input[i + 1][j + 1] == "S"
    ):
        return 1
    return 0


def checkDownward(input, i, j):
    if (
        input[i - 1][j - 1] == "M"
        and input[i - 1][j + 1] == "M"
        and input[i + 1][j - 1] == "S"
        and input[i + 1][j + 1] == "S"
    ):
        return 1
    return 0


def checkUpward(input, i, j):
    if (
        input[i - 1][j - 1] == "S"
        and input[i - 1][j + 1] == "S"
        and input[i + 1][j - 1] == "M"
        and input[i + 1][j + 1] == "M"
    ):
        return 1
    return 0


def checkLeftward(input, i, j):
    if (
        input[i - 1][j - 1] == "S"
        and input[i - 1][j + 1] == "M"
        and input[i + 1][j - 1] == "S"
        and input[i + 1][j + 1] == "M"
    ):
        return 1
    return 0


print(partOne())
print(partTwo())
