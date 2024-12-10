import numpy as np
import time
import heapq

f = open("./day_09/input.txt")
input = ""
for line in f:
    input = line.strip("\n")


def makeArrays(line):
    values = []
    blanks = []
    for i in range(len(line)):
        if i % 2 == 0:
            values.append(int(line[i]))
        else:
            blanks.append(int(line[i]))
    return (values, blanks)


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


def partOne(maxTries=100):
    (values, blanks) = makeArrays(input)
    frontLabel = 0
    backLabel = len(values) - 1
    location = 0
    checkSum = 0
    front = True
    while len(values) > 0:  # and location < maxTries:
        #       print(values, front, frontLabel, backLabel, location, checkSum)
        if front:
            if values[0] != 0:
                checkSum += location * frontLabel
                values[0] -= 1
                location += 1
            else:
                values.pop(0)
                frontLabel += 1
                front = False
        else:
            if values[-1] == 0:
                values.pop(-1)
                backLabel -= 1
            elif blanks[0] == 0:
                blanks.pop(0)
                front = True
            else:
                checkSum += location * backLabel
                values[-1] -= 1
                blanks[0] -= 1
                location += 1
    return checkSum


def partTwo():
    (values, blanks) = makeArrays(input)
    (blankStarts, valueStarts) = makeStarts(values, blanks)
    checkSum = 0
    for i in range(len(values))[::-1]:
        for j in range(len(blanks)):
            if (
                values[i] > 0
                and values[i] <= blanks[j]
                and valueStarts[i] > blankStarts[j]
            ):
                checkSum += i * sum(range(blankStarts[j], blankStarts[j] + values[i]))
                blankStarts[j] += values[i]
                blanks[j] -= values[i]
                values[i] = 0
    print(checkSum)
    for i in range(len(values)):
        if values[i] > 0:
            checkSum += i * sum(range(valueStarts[i], valueStarts[i] + values[i]))
    return checkSum


def partTwoBetter():
    (values, blanks) = makeArrays(input)
    (blankStarts, valueStarts) = makeStarts(values, blanks)
    heaps = buildHeaops(blanks, blankStarts)
    checkSum = 0
    for i in range(len(values))[::-1]:
        if values[i] > 0:
            target = getTarget(heaps, values[i], valueStarts[i])
            if target != -1:
                dest = heapq.heappop(heaps[target])
                checkSum += i * sum(range(dest, dest + values[i]))
                if target > values[i]:
                    heapq.heappush(heaps[target - values[i]], dest + values[i])
                values[i] = 0
    print(checkSum)
    for i in range(len(values)):
        if values[i] > 0:
            checkSum += i * sum(range(valueStarts[i], valueStarts[i] + values[i]))
    return checkSum


def buildHeaops(blanks, blankStarts):
    heaps = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for i in range(len(blanks)):
        if blanks[i] > 0:
            heaps[blanks[i]].append(blankStarts[i])
    return heaps


def getTarget(heaps, size, moveFrom):
    minHeap = size
    minVal = np.inf
    if size <= 9:
        for i in range(size, 10):
            if len(heaps[i]) > 0 and heaps[i][0] < minVal and heaps[i][0] < moveFrom:
                minHeap = i
                minVal = heaps[i][0]
    if minVal == np.inf:
        return -1
    return minHeap


def makeStarts(values, blanks):
    blankResult = []
    valueResult = []
    location = 0
    for i in range(len(values)):
        valueResult.append(location)
        location += values[i]
        blankResult.append(location)
        if i < len(blanks):
            location += blanks[i]
    return (blankResult, valueResult)


# print(partOne())
startTime = time.time()
print(partTwo())
print(time.time() - startTime)
startTime = time.time()
print(partTwoBetter())
print(time.time() - startTime)


# not 8591361868443
