from core.objects.block import Block

class Blockchain:
    difficulty = 0
    chain = []
    def __init__(self, difficulty):
        self.difficulty = difficulty
    def addblock(self, block):
        self.chain.append(block)

    def getblocknumber(self):
        if self.chain:
            return len(self.chain)
        else:
            return 0

    def showblockchain(self):
        print()
        for block in self.chain:
            block.visualize()
            print()
