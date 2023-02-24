from Block import Block

inputFile = open("input-generated.txt", "r")
curve =  [int(i) for i in inputFile.readline().split()]
lines = [line.rstrip() for line in inputFile]
blocks = [Block(i, int(b.split()[0]), int(b.split()[1]), int(b.split()[2])) for i, b in enumerate(lines)]

blocks.sort(key=lambda b: b.deadline)

solution = []

def pickBestBlock(blocks, currentTime, currentProd):
    bestArea = 0
    bestId = None
    for b in blocks:
        # if currentTime + b.base > b.deadline:
        #     print("exiting search")
        #     break
        if b.height <= currentProd:
            area = b.base * b.height
            if area > bestArea:
                bestId = b.id
    
    if (bestId is not None):
        return [b for b in blocks if b.id == bestId][0]
    return None


for i, value in enumerate(curve):
    selectedBlock = pickBestBlock(blocks, i, value)
    solution.append(selectedBlock)
    if selectedBlock is not None:
        blocks = [b for b in blocks if b.id != selectedBlock.id]

outputFile = open("output-generated.txt", "w")
for b in solution:
    if b is None:
        outputFile.write("\n")
    else:
        outputFile.write(str(b.id) + "\n")
outputFile.close()
