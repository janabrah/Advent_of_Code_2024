import numpy as np

f = open("./day_05/input.txt")
rules = []
pages = []
for line in f:
    if "|" in line:
        rules.append([int(i) for i in line.strip("\n").split("|")])
    elif "," in line:
        pages.append([int(i) for i in line.strip("\n").split(",")])


def makeRuleDict(rules):
    ruleDict = {}
    for rule in rules:
        if rule[1] not in ruleDict:
            ruleDict[rule[1]] = [rule[0]]
        else:
            ruleDict[rule[1]].append(rule[0])
    return ruleDict


def checkRow(ruleDict, page):
    illegals = {}
    for i in range(len(page)):
        if page[i] in illegals:
            return False
        for banned in ruleDict.get(page[i], []):
            illegals[banned] = page[i]
    return True


def partOne():
    ruleDict = makeRuleDict(rules)
    result = 0
    for page in pages:
        if checkRow(ruleDict, page):
            result += page[int((len(page) - 1) / 2)]
    return result


def getBads(ruleDict, pages):
    result = 0
    bads = []
    for page in pages:
        if not checkRow(ruleDict, page):
            bads.append(page)
    return bads


def fixPage(ruleDict, page):
    illegals = {}
    for i in range(len(page)):
        if page[i] in illegals:
            newPage = (
                page[: illegals[page[i]]]
                + [page[i]]
                + page[illegals[page[i]] : i]
                + page[i + 1 :]
            )
            return fixPage(ruleDict, newPage)
        for banned in ruleDict.get(page[i], []):
            illegals[banned] = i
    return page


def partTwo():
    ruleDict = makeRuleDict(rules)
    bads = getBads(ruleDict, pages)
    total = 0
    for bad in bads:
        good = fixPage(ruleDict, bad)
        total += good[int((len(good) - 1) / 2)]
    return total


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


print(rules)
print(pages)
print(makeRuleDict(rules))
print(partOne())
print(partTwo())
