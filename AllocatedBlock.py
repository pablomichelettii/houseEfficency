from Block import Block

class AllocatedBlock(Block):
    def __init__(self, block, currentTime):
        self.runtime = block.runtime
        self.id = block.id
        self.cost = block.cost
        self.deadline = block.deadline
        self.allocationTime = currentTime
        self.completionTime = currentTime + block.runtime
