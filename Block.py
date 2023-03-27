class Block:
    def __init__(self, id, runtime: int, cost: int, deadline: int):
        self.runtime: int = runtime
        self.id = id
        self.cost: int = cost
        self.deadline: int = deadline

    def __str__(self):
        return f"Block id: {self.id}, runtime: {self.runtime}, cost: {self.cost}, deadline: {self.deadline}"
