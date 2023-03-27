import sys
from Block import Block

DEBUG = False

def loadInput(inputPath):
    lines: list[str] = []
    blocks: list[Block] = []

    with open(inputPath) as file:
        lines = file.readlines()

    productionCurve = list(map(int, lines[0].split(" ")))
    lines.pop(0)

    for i in range(len(lines)):
        data = lines[i].split()

        runtime = data[0]
        cost = data[1]
        deadline = data[2]
        blocks.append(
            Block(
                i,
                int(runtime),
                int(cost),
                int(deadline),
            )
        )

    return productionCurve, blocks


def writeOutput(outputPath, tasksIds: list[list[Block]], prod):
    lines: list[str] = []

    with open(outputPath, "w") as f:
        for tasks in tasksIds:
            line = ""

            line = " ".join(str(task.id) for task in tasks)
            lines.append(line)

        f.write("\n".join(lines))


def createLog(
    id: int,
    consumption: int,
    production: int,
):
    msg: list[int] = []
    msg.append(id)
    msg.append(consumption)
    msg.append(production)

    return " ".join(map(lambda msg: str(msg), msg))


def simpleSorting(production, blocks: list[Block]) -> list[list[Block]]:
    allocatedBlocks: list[list[Block]] = []
    consumption = [0 for _ in range(len(production))]

    for i in range(len(production)):
        selectedBlocks: list[Block] = []

        for block in blocks:
            if block.deadline <= i + block.runtime:
                blocks.remove(block)
                continue

            if i + block.runtime > len(production):
                blocks.remove(block)
                continue

            if block.cost + consumption[0] < production[i]:
                selectedBlocks.append(block)
                blocks.remove(block)

                for j in range(selectedBlocks[-1].runtime):
                    consumption[j] += selectedBlocks[-1].cost

        if DEBUG:
            print(
                createLog(
                    i,
                    consumption[0],
                    production[i],
                )
            )

        allocatedBlocks.append(selectedBlocks)
        consumption.pop(0)

    return allocatedBlocks


if __name__ == "__main__":
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]

    production, tasks = loadInput(inputPath)

    tasks.sort(key=lambda t: t.deadline)
    tasks = simpleSorting(production, tasks)

    writeOutput(outputPath, tasks, production)
