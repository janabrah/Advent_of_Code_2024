import numpy as np

### This my very rushed version to get it in in 2.5 minutes, polished/more efficient version maybe to come later
f = open("input_01.txt")
input = []
left = []
right = []
for line in f:
    row = line.strip("\n").split("   ")
    left.append(int(row[0]))
    right.append(int(row[1]))
    input.append(
        [int(line.strip("\n").split("   ")[0]), int(line.strip("\n").split("   ")[1])]
    )


left.sort()
right.sort()
right = np.array(right)

## Part 1
res = 0
for i in range(len(left)):
    res += abs(left[i] - right[i])
print(res)


def prettyPrint(myArray):
    for row in myArray:
        print("".join([str(row[i]) for i in range(len(row))]))
    print()


## Part 2
res = 0
for entry in left:
    res += entry * np.count_nonzero(right == entry)
print(res)
