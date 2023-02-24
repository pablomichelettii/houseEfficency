
from Block import Block
from AllocatedBlock import AllocatedBlock
import matplotlib.pyplot as plt
import numpy as np

inputFile = open("input-generated.txt", "r")
curve =  [int(i) for i in inputFile.readline().split()]
lines = [line.rstrip() for line in inputFile]
blocks = [Block(i, int(b.split()[0]), int(b.split()[1]), int(b.split()[2])) for i, b in enumerate(lines)]


try:
    outputFile = open("output-generated.paolo.txt", "r")
    lines = [line.rstrip() for line in outputFile]

    schedule = []

    for l in lines:
        ids = [int(id) for id in l.split()]
        hour = [b for b in blocks if int(b.id) in ids]
        schedule.append(hour)

    # array of the equivalent consumption (summing all blocks for a unit of time)
    solution = []

    # pointer to current time
    currentTime = 0

    # array to host the blocks that have a base larger than 1 (that affect the following curve)
    oldBlocks = []

    for s in schedule:
        # check the schedule to sum the heights of the block that don't exceed the deadline, and the blocks that still affect the producion
        solution.append(sum([b.cost for b in schedule[currentTime] if b.deadline >= currentTime + b.runtime]) + sum(b.cost for b in oldBlocks))
        # add all the block that last for more than 1 to be considered in the next iterations
        oldBlocks.extend([AllocatedBlock(b, currentTime) for b in schedule[currentTime] if b.runtime > 1 and b.deadline >= currentTime + b.runtime])
        # increase the currentTime
        currentTime += 1
        # clean the blocks that have been completed
        oldBlocks = [b for b in oldBlocks if b.completionTime > currentTime]

    # drawing

    plt.step(np.array(range(0, len(curve))), np.array(curve), 'r', where='post')
    plt.bar(np.array(range(0, len(solution))), np.array(solution), align="edge", color="yellow")
    plt.show()

    
    score = 0
    for i, max in enumerate(curve):
        score += solution[i] if solution[i] <= curve[i] else curve[i] - (solution[i] - curve[i])

    print("Score: " + str(score))


except Exception as e:
    print(e)




