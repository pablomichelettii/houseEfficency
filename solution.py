import sys
from Block import Block
    
def loadInput(inputPath):
    with open(inputPath) as file:
        productionCurve = list(map(int, file.readline().strip().split()))
        lines = [line.rstrip() for line in file]
        blocks = [Block(i, int(b.split()[0]), int(b.split()[1]), int(b.split()[2])) for i, b in enumerate(lines)]
    return productionCurve, blocks

def writeOutput(outputPath,taskIds: list[Block], prod):
    with open(outputPath, "w") as f:
        f.write("\n".join(str(task.id) if task != None else "" for task in taskIds))
        
        print(len(taskIds))
        print(len(prod))

        for i in range(len(taskIds),len(prod)):
            f.write("\n")    
         
                
def simpleSort(blockA: Block):
    return blockA.deadline

def simpleSorting(production, blocks: list[Block]):
    allocatedBlocks: list[Block] = []
    consumed = [0 for _ in range(len(production))]

    for i in range(len(production)):
        selectedBlock:Block = None
        for block in blocks:
            if block.deadline <= i + block.runtime:
                blocks.remove(block)
                continue

            if block.cost + consumed[i] < production[i]:
                selectedBlock = block
                break

        allocatedBlocks.append(selectedBlock)

        if selectedBlock == None:
            continue

        # print(i)
        # print(f"cost: {selectedBlock.cost}")
        # print(f"duration: {selectedBlock.runtime}")
        # print(f"consumo: {consumed[i]}")
        # print(f"production: {production[i]}")
        # print()

        for j in range(i, i + blocks[0].runtime):
            if j > len(consumed) - 1:
                break
            consumed[j] += blocks[0].cost

        blocks.remove(blocks[0])
    return allocatedBlocks    

    
if __name__ == '__main__':
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    production, tasks = loadInput(inputPath)

    tasks.sort(key=lambda t: t.deadline)
    tasks = simpleSorting(production, tasks)

    tasks = tasks[:len(production)]
    writeOutput(outputPath, tasks, production)