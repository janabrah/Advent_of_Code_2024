import numpy as np

f = open("./day_07/input.txt")
input = []
for line in f:
    [result, equation] = line.strip("\n").split(": ")
    splitEquation = equation.split(" ")
    input.append((int(result), [int(i) for i in splitEquation]))


def partOne():
    total = 0
    for [res, eq] in input:
        if checkEquation(int(res), [int(i) for i in eq]):
            #            print("success")
            total += res
    #        else:
    #            print("fail")
    return total


def checkEquation(result, equation):
    if result < equation[0]:
        return False
    if len(equation) == 0 and result == 0:
        return True
    if len(equation) == 1:
        return result == equation[0]
    current = equation.pop(0)
    temp = [i for i in equation]
    temp[0] = temp[0] * current
    times = checkEquation(result, temp)
    temp = [i for i in equation]
    temp[0] = temp[0] + current
    plus = checkEquation(result, temp)
    return times or plus


def checkEquationTwo(result, equation):
    #    print(result, equation)
    if result < equation[0]:
        return False
    if len(equation) == 0 and result == 0:
        return True
    if len(equation) == 1:
        return result == equation[0]
    if sum(equation) == result:
        return True
    current = equation.pop(0)
    temp = [i for i in equation]
    temp[0] = temp[0] * current
    if checkEquationTwo(result, temp):
        return True
    temp = [i for i in equation]
    temp[0] = temp[0] + current
    if checkEquationTwo(result, temp):
        return True
    temp = [i for i in equation]
    temp[0] = int(str(current) + str(temp[0]))
    if checkEquationTwo(result, temp):
        return True
    return False


def partTwo():
    total = 0
    for [res, eq] in input:
        if checkEquationTwo(int(res), [int(i) for i in eq]):
            #            print("success")
            total += res
    #        else:
    #            print("fail")
    return total


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


print(partTwo())
