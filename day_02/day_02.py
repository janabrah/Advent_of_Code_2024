f = open("./day_02/input_02.txt")
input = []
for line in f:
    input.append([int(i) for i in line.strip("\n").split()])


def checkRow(row, graceUsed=False):
    trackers = [True, True]  # whether we might still be [growing, shrinking]
    for i in range(len(row) - 1):
        isShrinking = row[i + 1] < row[i]
        if not trackers[isShrinking]:
            if not graceUsed:
                return checkDeeper(row, i, i + 1)
            else:
                return False
        if trackers[not isShrinking] and not graceUsed:
            if checkRow(row[:i] + row[i + 1 :], True):
                return True
        trackers[not isShrinking] = False
        if not stepSize(row[i + 1], row[i]):
            if not graceUsed:
                return checkDeeper(row, i, i + 1)
            return False
    return True


def stepSize(next, current):
    return abs(next - current) >= 1 and abs(next - current) <= 3


def checkDeeper(row, candidate1, candidate2):
    success = False
    if candidate1 < len(row):
        success = success or checkRow(row[:candidate1] + row[candidate1 + 1 :], True)
    if (not success) and candidate2 < len(row):
        success = success or checkRow(row[:candidate2] + row[candidate2 + 1 :], True)
    return success


def partOne():
    count = 0
    for row in input:
        count += checkRow(row, True)
    return count


def partTwo():
    count = 0
    for row in input:
        count += checkRow(row, False)
    return count


print("Part 1 is " + str(partOne()))
print("Part 2 is " + str(partTwo()))
