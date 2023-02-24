import itertools
import numpy as np
from Block import Block
    
def loadInput(inputPath):
    with open(inputPath) as file:
        productionCurve = list(map(int, file.readline().strip().split()))
        lines = [line.rstrip() for line in file]
        blocks = [Block(i, int(b.split()[0]), int(b.split()[1]), int(b.split()[2])) for i, b in enumerate(lines)]
        # blocks.sort(key=lambda t: t.deadline)
        print(blocks)
    return productionCurve, blocks

def getEnergyProductionInRange(productionCurve, startRange, endRange):
    return sum(productionCurve[startRange:endRange])

def getTasksEnergyCostInRange(tasks: list[Block], startRange, endRange):
    energyCost = 0
    for task in tasks:
        if task.deadline < endRange:
            continue
        if task.deadline < startRange + task.runtime:
            energyCost =+ task.cost
    return energyCost

# questa roba è O(n)allamillemila 
def getTasksCombinations(tasks: list[Block], maxTasks):
    for i in range(1, maxTasks+1):
        for combination in itertools.combinations(tasks, i):
            yield combination


def getBestTasksCombinations(productionCurve, tasksCombinations, startRange, endRange):
    # giusto per partire uso che l'energia residua è infinita in negativo per comoditá
    bestEnergyResidual = -np.inf
    bestTaskCombination = None
    for tasksCombination in tasksCombinations:
        energyCost = getTasksEnergyCostInRange(tasksCombination, startRange, endRange)
        energyProduction = getEnergyProductionInRange(productionCurve, startRange, endRange)
        energyResidual = energyProduction - energyCost
        if energyResidual > bestEnergyResidual:
            bestEnergyResidual = energyResidual
            bestTaskCombination = tasksCombination
        return bestTaskCombination

def scheduleTasks(productionCurve, tasks: list[Block]):
    taskIds = []
    # iterazione delle unitá temporali
    for i in range(len(productionCurve)):
        bestEnergyResidual = -np.inf
        bestTasksCombination = None
        for j in range(i+1):
            taskCombinations = getTasksCombinations(tasks, i-j+1)
            taskCombination = getBestTasksCombinations(productionCurve, taskCombinations, j, i+1)
            energyCost = getTasksEnergyCostInRange(taskCombination, j, i+1)
            energyProduction = getEnergyProductionInRange(productionCurve, j, i+1)
            energyResidual = energyProduction - energyCost
            if energyResidual > bestEnergyResidual:
                bestEnergyResidual = energyResidual
                bestTasksCombination = taskCombination
        if bestTasksCombination is not None:
            taskIds.append([task.id for task in bestTasksCombination])
            for task in bestTasksCombination:
                tasks.remove(task)
        else:
            taskIds.append([])
    return taskIds

def writeOutput(outputPath, taskIds):
    with open(outputPath, "w") as f:
        for taskId in taskIds:
            if taskId is None:
                f.write("\n")
            else:
                f.write("".join(str(id) for id in taskId) + "\n")


if __name__ == '__main__':
    inputPath = "input-generated.txt"
    outputPath = "output-generated.paolo.txt"
    production, tasks = loadInput(inputPath)
    taskIds = scheduleTasks(production, tasks)
    writeOutput(outputPath, taskIds)