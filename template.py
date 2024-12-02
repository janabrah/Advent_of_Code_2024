import numpy as np

f = open("./day_xx/input.txt")
input = []
for line in f:
    input.append([int(i) for i in line.strip("\n").split()])


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()
