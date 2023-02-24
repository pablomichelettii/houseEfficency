from Block import Block

class AllocatedBlock(Block):
    def __init__(self, block, currentTime):
        self.base = block.base
        self.id = block.id
        self.height = block.height
        self.deadline = block.deadline
        self.allocationTime = currentTime
        self.completionTime = currentTime + block.base
