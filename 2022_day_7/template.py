import numpy as np

f = open("./2022_day_7/input.txt")
input = []
for line in f:
    input.append(line.strip("\n"))


def partOne(input):
    data = buildJSON(input)
    print(data)
    print(data["/"])
    tot = 0
    for dir in data:
        if data[dir]["size"] == None:
            data[dir]["size"] = getDirSize(data, dir)
        if data[dir]["size"] <= 100000:
            print(data[dir])
            tot += data[dir]["size"]
    print(tot)


def buildJSON(input):
    data = {}
    subdir = {"dirs": [], "files": [], "size": None}
    workingOn = "root"
    for i in range(len(input) - 1):
        print(input[i])
        print(subdir)
        if input[i][:4] == "$ cd":
            print("inCd")
            if subdir["dirs"] != [] or subdir["files"] != []:
                data[workingOn] = subdir
            if input[i] != "$ cd ..":
                workingOn = input[i][5:]
            else:
                workingOn = "root"
            if input[i] != "$ cd /":
                subdir = {"dirs": [], "files": [], "size": None}
        elif input[i][0] != "$":
            row = input[i].split(" ")
            print(row)
            if row[0] == "dir":
                subdir["dirs"].append(row[1])
            else:
                subdir["files"].append(row)
    if subdir["dirs"] != [] or subdir["files"] != []:
        data[workingOn] = subdir
    return data


def getDirSize(data, dirName):
    size = 0
    for dir in data[dirName]["dirs"]:
        if dir in data:
            if data[dir]["size"] is None:
                data[dir]["size"] = getDirSize(data, dir)
            size += data[dir]["size"]
    for file in data[dirName]["files"]:
        size += int(file[0])
    return size


partOne(input)

# print(input)
