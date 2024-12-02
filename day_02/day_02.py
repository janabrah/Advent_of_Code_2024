# import numpy as np

f = open("input_02.txt")
input = []
for line in f:
    input.append([int(i) for i in line.strip("\n").split()])


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def checkRow(row, grace=False):
    print(row)
    growing = True
    shrinking = True
    if not grace and (checkRow(row[:-1], True) or checkRow(row[1:], True)):
        return True
    for i in range(len(row) - 1):
        if row[i + 1] < row[i]:
            if not shrinking:
                print("not shrinking" + str(grace))
                if not grace:
                    return checkRow(row[:i] + row[i + 1 :], True) or checkRow(
                        row[: i + 1] + row[i + 2 :], True
                    )
                return False
            if growing and (not grace) and checkRow(row[:i] + row[i + 1 :], True):
                return True
            growing = False
        elif row[i + 1] > row[i]:
            if not growing:
                print("not growing" + str(grace))
                if not grace:
                    return checkRow(row[:i] + row[i + 1 :], True) or checkRow(
                        row[: i + 1] + row[i + 2 :], True
                    )
                return False
            if shrinking and (not grace) and checkRow(row[:i] + row[i + 1 :], True):
                return True
            shrinking = False
        if not (abs(row[i + 1] - row[i]) >= 1 and abs(row[i + 1] - row[i]) <= 3):
            print("wrong spacing" + str(grace))
            if not grace:
                return checkRow(row[:i] + row[i + 1 :], True) or checkRow(
                    row[: i + 1] + row[i + 2 :], True
                )
            return False
    return True


count = 0
for row in input:
    count += checkRow(row)
print(count)

# print(input[:5])
