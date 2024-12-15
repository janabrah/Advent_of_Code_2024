import numpy as np
import math
import time


def loadInput(filename):
    f = open("./day_11/" + filename + ".txt")
    myList = []
    for line in f:
        myList.append([int(i) for i in line.strip("\n").split()])
    return myList[0]


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def blinkNumber(number):
    if number == 0:
        return [1]
    digitCount = math.ceil(math.log10(number + 1))
    if digitCount % 2 == 1:
        return [number * 2024]
    else:
        right = number % 10 ** (digitCount / 2)
        left = (number - right) // 10 ** (digitCount / 2)
        return [left, right]


def iterateBlink(number, blinks):
    growth = [1]
    numbers = [number]
    for i in range(blinks):
        #        print(numbers)
        newNumbers = []
        for number in numbers:
            newNumbers += blinkNumber(number)
        growth.append(len(newNumbers))
        numbers = newNumbers
    return growth[-1]


def partOne(blinks):
    myList = loadInput("input")
    total = 0
    for number in myList:
        total += iterateBlink(number, blinks)
    return total


def partTwo(blinks):
    numberDict = {}
    myList = loadInput("input")
    for number in myList:
        numberDict[number] = 1
    for blink in range(blinks):
        numberDict = singleBlink(numberDict)
    return sum(numberDict.values())


def singleBlink(numberDict):
    resultDict = {}
    for number in numberDict.keys():
        newNums = blinkNumber(number)
        for newNum in newNums:
            resultDict[newNum] = resultDict.get(newNum, 0) + numberDict[number]
    return resultDict


for count in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
    t = time.time()
    print(partTwo(count))
    print(count, time.time() - t)
