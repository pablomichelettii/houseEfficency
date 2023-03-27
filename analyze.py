import sys


class Day:
    def __init__(
        self,
        id: int,
        consumption: int,
        production: int,
    ) -> None:
        self.id = id
        self.consumption = consumption
        self.production = production


def loadInput(inputPath):
    days: list[Day] = []
    with open(inputPath) as file:

        for line in file.readlines():
            data = line.split(" ")

            if not data:
                continue

            days.append(
                Day(
                    int(data[0]),
                    int(data[1]),
                    int(data[2]),
                )
            )

    return days


def findSpike(days: list[Day]):
    print("spike")
    ids: list[int] = []

    for day in days:
        if day.consumption > day.production:
            ids.append(day.id)

    print("\n".join(map(lambda ids: str(ids), ids)))


if __name__ == "__main__":
    inputPath = sys.argv[1]

    days: list[Day] = loadInput(inputPath)

    findSpike(days)
