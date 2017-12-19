from core.objects.block import Block

class Blockchain:
    difficulty = 0
    chain = []
    def __init__(self, difficulty):
        self.difficulty = difficulty
