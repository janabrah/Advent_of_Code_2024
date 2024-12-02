import numpy as np

f = open("./day_03/input.txt")
input = []
for line in f:
    input.append(line.strip("\n"))


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()
